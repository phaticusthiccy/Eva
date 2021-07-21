default:
	terraform init
	terraform validate
	terraform apply -auto-approve
ORG := me
NAME := deployconfig
VERSION := 0.0.1
ARCH := darwin_amd64

BINARY := terraform-provider-$(NAME)_v0.0.1

deafult: $(BINARY)

install: $(BINARY)
	mkdir -p $(HOME)/.terraform.d/plugins/$(ORG)/$(NAME)/$(VERSION)/$(ARCH)
	cp $(BINARY) $(HOME)/.terraform.d/plugins/$(ORG)/$(NAME)/$(VERSION)/$(ARCH)/$(BINARY)

clean:
	rm -f $(HOME)/.terraform.d/plugins/$(ORG)/$(NAME)/$(VERSION)/$(ARCH)/$(BINARY)

$(BINARY): *.go
	go build -o $@ .
