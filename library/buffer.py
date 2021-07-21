# coding: utf-8
# based on Cethric's image capture gist....
FRAME_PROC_INTERVAL=15 #num frames to skip. 1=go as fast as possible, 5=every fifth frame
import ui
from objc_util import *
import ctypes
from objc_util import autoreleasepool
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
AVCaptureStillImageOutput = ObjCClass('AVCaptureStillImageOutput')
AVCaptureConnection = ObjCClass('AVCaptureConnection')
UIImage = ObjCClass('UIImage')
CIImage    = ObjCClass('CIImage')
CIDetector = ObjCClass('CIDetector')

CIDetectorTypeRectangle=ObjCInstance(c_void_p.in_dll(c,'CIDetectorTypeRectangle'))
CIDetectorTypeFace=ObjCInstance(c_void_p.in_dll(c,'CIDetectorTypeFace'))

kCGBitmapAlphaInfoMask = 0x1F
kCGBitmapFloatComponents = 1 << 8
kCGBitmapByteOrderMask = 0x7000
kCGBitmapByteOrderDefault = 0 << 12
kCGBitmapByteOrder16Little = 1 << 12
kCGBitmapByteOrder32Little = 2 << 12
kCGBitmapByteOrder16Big = 3 << 12
kCGBitmapByteOrder32Big = 4 << 12

kCGImageAlphaNone = 0
kCGImageAlphaPremultipliedLast = 1
kCGImageAlphaPremultipliedFirst = 2
kCGImageAlphaLast = 3
kCGImageAlphaFirst = 4
kCGImageAlphaNoneSkipLast = 5
kCGImageAlphaNoneSkipFirst = 6
kCGImageAlphaOnly = 7

kDroppedFrameReason = ObjCInstance(c_void_p.in_dll(c,'kCMSampleBufferAttachmentKey_DroppedFrameReason'))

CMGetAttachment = c.CMGetAttachment
CMGetAttachment.argtypes = [c_void_p, c_void_p, c_void_p]
CMGetAttachment.restype = c_void_p

class CMTime(ctypes.Structure):
    _fields_ = [
                ('CMTimeValue', ctypes.c_int64),
                ('CMTimeScale', ctypes.c_int32),
                ('CMTimeEpoch', ctypes.c_int64),
                ('CMTimeFlags', ctypes.c_uint32),
                ]
                
def CMTimeMake(value, scale):
    cm = CMTime()
    cm.CMTimeScale = scale
    cm.CMTimeValue = value
    return cm

def dispatch_queue_create(name, parent):
    func = c.dispatch_queue_create
    func.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(name, parent))
def dispatch_get_current_queue():
    func=c.dispatch_get_current_queue
    func.argtypes=[] 
    func.restype=c_void_p
    return ObjCInstance(func())

    
def dispatch_release(queue_obj):
    #raise RuntimeError('This is not the method you are looking for')
    func = c.dispatch_release
    func.argtyps = [ctypes.c_void_p]
    func.restype = None
    return func(ObjCInstance(queue_obj).ptr)
    
def CMSampleBufferGetImageBuffer(buffer):
    func = c.CMSampleBufferGetImageBuffer
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(buffer))
    
def CVPixelBufferLockBaseAddress(imagebuffer, param_0):
    func = c.CVPixelBufferLockBaseAddress
    func.argtypes = [ctypes.c_void_p, ctypes.c_int]
    func.restype = None
    return func(ObjCInstance(imagebuffer).ptr, param_0)

def CVPixelBufferUnlockBaseAddress(imagebuffer, param_0):
    func = c.CVPixelBufferUnlockBaseAddress
    func.argtypes = [ctypes.c_void_p, ctypes.c_int]
    func.restype = None
    return func(ObjCInstance(imagebuffer).ptr, param_0)
    
def CVPixelBufferGetBaseAddress(imagebuffer):
    func = c.CVPixelBufferGetBaseAddress
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_void_p
    return func(ObjCInstance(imagebuffer).ptr)

def CVPixelBufferGetBytesPerRow(imagebuffer):
    func = c.CVPixelBufferGetBytesPerRow
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_int
    return func(ObjCInstance(imagebuffer).ptr)

def CVPixelBufferGetWidth(imagebuffer):
    func = c.CVPixelBufferGetWidth
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_int
    return func(ObjCInstance(imagebuffer).ptr)
    
def CVPixelBufferGetHeight(imagebuffer):
    func = c.CVPixelBufferGetHeight
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_int
    return func(ObjCInstance(imagebuffer).ptr)
    
def CGColorSpaceCreateDeviceRGB():
    func = c.CGColorSpaceCreateDeviceRGB
    func.argtypes = None
    func.restype = ctypes.c_void_p
    return ObjCInstance(func())
    
def CGBitmapContextCreate(baseAddress, width, height, param_0, bytesPerRow, colorSpace, flags):
    func = c.CGBitmapContextCreate
    func.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int32]
    func.restype = ctypes.c_void_p
    result = func(baseAddress, int(width), int(height), int(param_0), int(bytesPerRow), ObjCInstance(colorSpace).ptr, flags)
    if result is not None:
        return ObjCInstance(result)
    else:
        raise RuntimeError('Failed to create context')
        
def CGContextRelease(context):
    func = c.CGContextRelease
    func.argtypes = [ctypes.c_void_p]
    func.restype = None
    return func(ObjCInstance(context).ptr)
    
def CGColorSpaceRelease(colorSpace):
    func = c.CGColorSpaceRelease
    func.argtypes = [ctypes.c_void_p]
    func.restype = None
    return func(ObjCInstance(colorSpace))
        
def CGBitmapContextCreateImage(context):
    func = c.CGBitmapContextCreateImage
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(ObjCInstance(context).ptr))
    
def CGImageRelease(image):
    func = c.CGImageRelease
    func.argtypes = [ctypes.c_void_p]
    func.restype = None
    return func(ObjCInstance(image).ptr)
    
def UIImageFromSampleBuffer(buffer):
    imagebuffer =  CMSampleBufferGetImageBuffer(buffer)
    CVPixelBufferLockBaseAddress(imagebuffer, 0)
    baseAddress = CVPixelBufferGetBaseAddress(imagebuffer)
    width = CVPixelBufferGetWidth(imagebuffer)
    height = CVPixelBufferGetHeight(imagebuffer)
    colorSpace = CGColorSpaceCreateDeviceRGB()
    flags = kCGBitmapByteOrderDefault | kCGImageAlphaNoneSkipFirst
    context = CGBitmapContextCreate(baseAddress, width / 4, height / 4, 8, 4 * width, colorSpace, flags)
    quartzImage = CGBitmapContextCreateImage(context)
    CVPixelBufferUnlockBaseAddress(imagebuffer, 0)
    CGContextRelease(context)
    CGColorSpaceRelease(colorSpace)
    image = UIImage.imageWithCGImage_(quartzImage)
    CGImageRelease(quartzImage)
    return image
    
def UIImagePNGRepresentation(image):
    func = c.UIImagePNGRepresentation
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(ObjCInstance(image).ptr))
    
def UIImageJPEGRepresentation(image, scale=32):
    func = c.UIImageJPEGRepresentation
    func.argtypes = [ctypes.c_void_p, ctypes.c_float]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(ObjCInstance(image).ptr, scale))
    
    
def detect_faces(samplebuffer):
    imagebuffer =  CMSampleBufferGetImageBuffer(samplebuffer)
    CVPixelBufferLockBaseAddress(imagebuffer, 0)
    baseAddress = CVPixelBufferGetBaseAddress(imagebuffer)
    width = CVPixelBufferGetWidth(imagebuffer)
    height = CVPixelBufferGetHeight(imagebuffer)
    ciimage = CIImage.imageWithCVPixelBuffer_((imagebuffer))
    options = {'CIDetectorAccuracy': 'CIDetectorAccuracyHigh'}
    face_detector = CIDetector.detectorOfType_context_options_('CIDetectorTypeFace', None, options)
    rectangle_detector = CIDetector.detectorOfType_context_options_('CIDetectorTypeRectangle', None, options)

    faces = face_detector.featuresInImage_(ciimage)
    #if faces:
    #   faces=list(ObjCInstance(faces))
    #else:
    faces=[]
    rects = rectangle_detector.featuresInImage_(ciimage)
    if rects:
       rects=list(ObjCInstance(rects))
    else:
       rects=[]

    CVPixelBufferUnlockBaseAddress(imagebuffer, 0)
    return faces, rects, (width, height)

view = None

@on_main_thread
def change_image(image):
    if view is not None:
        ObjCInstance(view['imageview1']).setImage_(ObjCInstance(image))
        # view['imageview1'].image = ui.Image.named('test.png')
@on_main_thread
def set_label(txt):
    if view is not None:
        view['lbl'].text=txt
import time
@on_main_thread
def compute_fps():
    a=.1   # ewma coefficient to smooth fps display
    if view is not None:
         t=time.perf_counter()
         view.fps=a/(t-view.last_time)+(1-a)*view.fps
         view.last_time=t
         faces=getattr(view,'faces',[])
         rects=getattr(view, 'rects',[]) 
         view.heartbeat=(view.heartbeat+1)%2
         error_str=''
         set_label(
         	'fps={:0.1f} proc:{:9d} faces:{} rects:{} {} {}'.format(view.fps,view.processed_frames, len(faces),len(rects),view.heartbeat, error_str))


         
def captureOutput_didOutputSampleBuffer_fromConnection_(_cmd, _self, _output, _buffer, _connection):
      view.frame_count=(view.frame_count+1)
      if view.frame_count>=FRAME_PROC_INTERVAL:
         view.frame_count=0
         buffer = ObjCInstance(_buffer)
         #image = UIImageFromSampleBuffer(buffer)
         faces,rects, image_size=detect_faces(buffer)
         view.faces=faces
         view.rects=rects
         view.image_size=image_size
         view.processed_frames=view.processed_frames+1
         #imageRep = UIImagePNGRepresentation(image)
         #imageRep = UIImageJPEGRepresentation(image)
         #imageRep.writeToFile_atomically_('test.png', True)
         #imageRep.writeToFile_atomically_('test.jpg', True)
         #change_image(image)
      compute_fps()
      pv.set_needs_display()
      

def captureOutput_didDropSampleBuffer_fromConnection_(_self,_cmd,output, sample_buffer, conn):
    reason=CMGetAttachment(sample_buffer, kDroppedFrameReason, None)
    view.frame_count=(view.frame_count+1)
    if reason:
         faces=getattr(view,'faces',[])
         rects=getattr(view, 'rects',[]) 
         error_str=str(ObjCInstance(reason))
         set_label(
         	'fps={:0.1f} proc:{:9d} faces:{} rects:{} {} {}'.format(view.fps,view.processed_frames, len(faces),len(rects),view.heartbeat, error_str))
         	
delegate_call = create_objc_class('delegate_call', protocols=['AVCaptureVideoDataOutputSampleBufferDelegate'], methods=[captureOutput_didOutputSampleBuffer_fromConnection_,
					captureOutput_didDropSampleBuffer_fromConnection_])
DESIRED_FPS = 5
@on_main_thread
def set_frame_rate(inputDevice, captureSession, desired_fps):
    #this doesnt seem to work at all!
    supported_rates=inputDevice.activeFormat().videoSupportedFrameRateRanges()[0]
    #print('min support',supported_rates.minFrameRate())
    if (desired_fps) <= supported_rates.maxFrameRate() and desired_fps >= supported_rates.minFrameRate():
        desired_intervalnum=600//desired_fps
        err_ptr = c_void_p()
        captureSession.beginConfiguration()

        inputDevice.lockForConfiguration_(byref(err_ptr))
        if err_ptr:
            raise()
        inputDevice.setActiveVideoMinFrameDuration_((desired_intervalnum,600,0,0))
        #print('a,b',inputDevice.activeVideoMinFrameDuration().a ,inputDevice.activeVideoMinFrameDuration().b)
        inputDevice.setActiveVideoMinFrameDuration_((desired_intervalnum,600,0,0))
        inputDevice.unlockForConfiguration()
        captureSession.commitConfiguration()
        #print('a,b',inputDevice.activeVideoMinFrameDuration().a ,inputDevice.activeVideoMinFrameDuration().b)
        
class CameraView(ui.View):
    @on_main_thread
    def __init__(self, *args, **kwargs):
        ui.View.__init__(self, *args, **kwargs)
        
        self.inputDevice = AVCaptureDevice.devices()[0]
        

        #(CMTimeMake(2,1), argtypes=[CMTime], restype=None)
        
        self.captureInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(self.inputDevice, None)

        if not self.captureInput:
            print('Failed to create device')
            exit()
    
        self.captureOutput = AVCaptureVideoDataOutput.alloc().init()
        self.captureSession = AVCaptureSession.alloc().init()
        self.captureSession.setSessionPreset_('AVCaptureSessionPresetHigh')
        
        if self.captureSession.canAddInput_(self.captureInput):
            self.captureSession.addInput_(self.captureInput)
    
        if self.captureSession.canAddOutput_(self.captureOutput):
            self.captureSession.addOutput_(self.captureOutput)

        
        self.captureVideoPreviewLayer = AVCaptureVideoPreviewLayer.layerWithSession_(self.captureSession)
        
        queue_test = dispatch_queue_create(b'imageDispatch', None)
        #queue_test = dispatch_get_current_queue()

        
        #self.inputDevice.lockForConfiguration_(None)

        
        print(self.captureOutput.connections()[0].videoMinFrameDuration().a)
        callback = delegate_call.alloc().init()
        self.captureOutput.setSampleBufferDelegate_queue_(callback, queue_test)
        self.queue=queue_test
        
    def present(self, *args, **kwargs):
        ui.View.present(self, *args, **kwargs)
        self.set_layer()
    
    @on_main_thread
    def set_layer(self):
        v = ObjCInstance(self)
        self.captureVideoPreviewLayer.setFrame_(v.bounds())
        self.captureVideoPreviewLayer.setVideoGravity_('AVLayerVideoGravityResizeAspectFill')
        v.layer().addSublayer_(self.captureVideoPreviewLayer)
        set_frame_rate(self.inputDevice,self.captureSession, DESIRED_FPS)
        self.captureSession.startRunning()
    
    @on_main_thread
    def will_close(self):
        self.captureSession.stopRunning()
        dispatch_release(self.queue)
        
class PathView(ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def draw_rects(self, rects, color):
      ui.set_color(color)
      for rect in rects:
          rect_bounds = rect.bounds()
          # View は X軸=375 Y軸=667
          # 画像のX軸Y軸をViewのY軸X軸に対応させ、サイズを調整
          x = rect_bounds.origin.y    * self.height / view.image_size[0]
          y = rect_bounds.origin.x    * self.width  / view.image_size[1]
          w = rect_bounds.size.height * self.height / view.image_size[0]
          h = rect_bounds.size.width  * self.width  / view.image_size[1]
          print(x,y,w,h)
          path = ui.Path.rect(x, y, w * 1.3, h)
          path.fill()
      path=ui.Path.rect(100,100,200,200).stroke()

    def draw(self):
      self.draw_rects(view.rects, (1,0,0,0.5))
      self.draw_rects(view.faces, (0,1,0,0.5))

      
class CustomView(ui.View):
    def __init__(self, *args, **kwargs):
        ui.View.__init__(self, *args, **kwargs)
        self.frame = (0,0, 800,600)
        self.fps=0
        self.heartbeat=0
        self.frame_count=0
        self.processed_frames=0
        self.last_time=time.perf_counter()
        self.faces=[]
        self.rects=[]
        
    def did_load(self):
        self['camera'].set_layer()
        #self['imageview1'].image = ui.Image.named('test:Numbers')
        
    def present(self, *args, **kwargs):
        ui.View.present(self, *args, **kwargs)
        
    def will_close(self):
        self['camera'].will_close()
        


view=CustomView()
cv=CameraView(frame=(0,0,400,600), name='camera')
pv=PathView(frame=(0,0,400,600), name='path')
#iv=ui.ImageView(name='imageview1', frame=(400,0,400,600))
lbl=ui.Label(name='lbl',frame=(0,0,800,200))
lbl.text_color='#fbff99'
view.add_subview(cv)
view.add_subview(pv)
#view.add_subview(iv)
view.add_subview(lbl)
view.did_load()
view.present()
