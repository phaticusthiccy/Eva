default:
	terraform init
	terraform validate
	terraform apply -auto-approve
ORG := Eva 
NAME := deployconfig
VERSION := 0.0.2
ARCH := arch_amd64-x86

BINARY := terraform-provider-$(NAME)_v0.0.2

deafult: $(BINARY)

install: $(BINARY)
	mkdir -p $(HOME)/.terraform.d/plugins/$(ORG)/$(NAME)/$(VERSION)/$(ARCH)
	cp $(BINARY) $(HOME)/.terraform.d/plugins/$(ORG)/$(NAME)/$(VERSION)/$(ARCH)/$(BINARY)
        mkdir -p /root/
clean:
	rm -f $(HOME)/.terraform.d/plugins/$(ORG)/$(NAME)/$(VERSION)/$(ARCH)/$(BINARY)

$(BINARY): *.go
	go build -o $@ .
