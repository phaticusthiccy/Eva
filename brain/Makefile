# The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
# The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
# Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
# All such material is used with the permission of the owner.
# All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
# All Rights Reserved.

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
