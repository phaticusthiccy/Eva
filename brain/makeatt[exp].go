/*
The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
All such material is used with the permission of the owner.
All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
All Rights Reserved.
*/


package main

import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

// Provider -
func Provider() *schema.Provider {
	return &schema.Provider{
		ResourcesMap: map[string]*schema.Resource{},
		DataSourcesMap: map[string]*schema.Resource{
			"custom_deploy_config": dataSourceCustomDeployConfig(),
		},
	}
}
