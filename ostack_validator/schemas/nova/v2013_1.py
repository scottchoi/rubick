from ostack_validator.schema import ConfigSchemaRegistry

nova = ConfigSchemaRegistry.register_schema(project='nova')

nova.version('2013.1')
nova.section('DEFAULT')

#
# Options defined in nova.availability_zones
#

# availability_zone to show internal services under (string
# value)
nova.param('internal_service_availability_zone', type='string', default='internal')

# default compute node availability_zone (string value)
#default_availability_zone=nova
nova.param('default_availability_zone', type='string', default='nova')


#
# Options defined in nova.crypto
#

# Filename of root CA (string value)
#ca_file=cacert.pem

# Filename of private key (string value)
#key_file=private/cakey.pem

# Filename of root Certificate Revocation List (string value)
#crl_file=crl.pem

# Where we keep our keys (string value)
#keys_path=$state_path/keys

# Where we keep our root CA (string value)
#ca_path=$state_path/CA

# Should we use a CA for each project? (boolean value)
#use_project_ca=false

# Subject for certificate for users, %s for project, user,
# timestamp (string value)
#user_cert_subject=/C=US/ST=California/O=OpenStack/OU=NovaDev/CN=%.16s-%.16s-%s

# Subject for certificate for projects, %s for project,
# timestamp (string value)
#project_cert_subject=/C=US/ST=California/O=OpenStack/OU=NovaDev/CN=project-ca-%.16s-%s


#
# Options defined in nova.exception
#

# make exception message format errors fatal (boolean value)
#fatal_exception_format_errors=false


#
# Options defined in nova.netconf
#

# ip address of this host (string value)
#my_ip=10.0.0.1

# Name of this node.  This can be an opaque identifier.  It is
# not necessarily a hostname, FQDN, or IP address. However,
# the node name must be valid within an AMQP key, and if using
# ZeroMQ, a valid hostname, FQDN, or IP address (string value)
#host=nova
nova.param('host', type='string')

nova.param('use_ipv6', type='boolean')


#
# Options defined in nova.notifications
#

# If set, send compute.instance.update notifications on
# instance state changes.  Valid values are None for no
# notifications, "vm_state" for notifications on VM state
# changes, or "vm_and_task_state" for notifications on VM and
# task state changes. (string value)
#notify_on_state_change=<None>

# If set, send api.fault notifications on caught exceptions in
# the API service. (boolean value)
#notify_api_faults=false


#
# Options defined in nova.paths
#

# Directory where the nova python module is installed (string
# value)
#pybasedir=/usr/lib/python/site-packages

# Directory where nova binaries are installed (string value)
#bindir=/usr/local/bin

# Top-level directory for maintaining nova's state (string
# value)
#state_path=$pybasedir


#
# Options defined in nova.policy
#

# JSON file representing policy (string value)
#policy_file=policy.json

# Rule checked when requested rule is not found (string value)
#policy_default_rule=default


#
# Options defined in nova.quota
#

# number of instances allowed per project (integer value)
#quota_instances=10

# number of instance cores allowed per project (integer value)
#quota_cores=20

# megabytes of instance ram allowed per project (integer
# value)
#quota_ram=51200

# number of floating ips allowed per project (integer value)
#quota_floating_ips=10

# number of fixed ips allowed per project (this should be at
# least the number of instances allowed) (integer value)
#quota_fixed_ips=-1

# number of metadata items allowed per instance (integer
# value)
#quota_metadata_items=128

# number of injected files allowed (integer value)
#quota_injected_files=5

# number of bytes allowed per injected file (integer value)
#quota_injected_file_content_bytes=10240

# number of bytes allowed per injected file path (integer
# value)
#quota_injected_file_path_bytes=255

# number of security groups per project (integer value)
#quota_security_groups=10

# number of security rules per security group (integer value)
#quota_security_group_rules=20

# number of key pairs per user (integer value)
#quota_key_pairs=100

# number of seconds until a reservation expires (integer
# value)
#reservation_expire=86400

# count of reservations until usage is refreshed (integer
# value)
#until_refresh=0

# number of seconds between subsequent usage refreshes
# (integer value)
#max_age=0

# default driver to use for quota checks (string value)
#quota_driver=nova.quota.DbQuotaDriver


#
# Options defined in nova.service
#

# seconds between nodes reporting state to datastore (integer
# value)
#report_interval=10

# enable periodic tasks (boolean value)
#periodic_enable=true

# range of seconds to randomly delay when starting the
# periodic task scheduler to reduce stampeding. (Disable by
# setting to 0) (integer value)
#periodic_fuzzy_delay=60

# a list of APIs to enable by default (list value)
#enabled_apis=ec2,osapi_compute,metadata

# a list of APIs with enabled SSL (list value)
#enabled_ssl_apis=

# IP address for EC2 API to listen (string value)
#ec2_listen=0.0.0.0

# port for ec2 api to listen (integer value)
#ec2_listen_port=8773

# Number of workers for EC2 API service (integer value)
#ec2_workers=<None>

# IP address for OpenStack API to listen (string value)
#osapi_compute_listen=0.0.0.0

# list port for osapi compute (integer value)
#osapi_compute_listen_port=8774

# Number of workers for OpenStack API service (integer value)
#osapi_compute_workers=<None>

# OpenStack metadata service manager (string value)
#metadata_manager=nova.api.manager.MetadataManager

# IP address for metadata api to listen (string value)
#metadata_listen=0.0.0.0

# port for metadata api to listen (integer value)
#metadata_listen_port=8775

# Number of workers for metadata service (integer value)
#metadata_workers=<None>

# full class name for the Manager for compute (string value)
#compute_manager=nova.compute.manager.ComputeManager

# full class name for the Manager for console proxy (string
# value)
#console_manager=nova.console.manager.ConsoleProxyManager

# full class name for the Manager for cert (string value)
#cert_manager=nova.cert.manager.CertManager

# full class name for the Manager for network (string value)
#network_manager=nova.network.manager.VlanManager

# full class name for the Manager for scheduler (string value)
#scheduler_manager=nova.scheduler.manager.SchedulerManager

# maximum time since last check-in for up service (integer
# value)
#service_down_time=60


#
# Options defined in nova.test
#

# File name of clean sqlite db (string value)
#sqlite_clean_db=clean.sqlite


#
# Options defined in nova.utils
#

# Whether to log monkey patching (boolean value)
#monkey_patch=false

# List of modules/decorators to monkey patch (list value)
#monkey_patch_modules=nova.api.ec2.cloud:nova.notifications.notify_decorator,nova.compute.api:nova.notifications.notify_decorator

# Length of generated instance admin passwords (integer value)
#password_length=12

# time period to generate instance usages for.  Time period
# must be hour, day, month or year (string value)
#instance_usage_audit_period=month

# Path to the rootwrap configuration file to use for running
# commands as root (string value)
#rootwrap_config=/etc/nova/rootwrap.conf

# Explicitly specify the temporary working directory (string
# value)
#tempdir=<None>


#
# Options defined in nova.wsgi
#

# File name for the paste.deploy config for nova-api (string
# value)
#api_paste_config=api-paste.ini

# A python format string that is used as the template to
# generate log lines. The following values can be formatted
# into it: client_ip, date_time, request_line, status_code,
# body_length, wall_seconds. (string value)
#wsgi_log_format=%(client_ip)s "%(request_line)s" status: %(status_code)s len: %(body_length)s time: %(wall_seconds).7f

# CA certificate file to use to verify connecting clients
# (string value)
#ssl_ca_file=<None>

# SSL certificate of API server (string value)
#ssl_cert_file=<None>

# SSL private key of API server (string value)
#ssl_key_file=<None>

# Sets the value of TCP_KEEPIDLE in seconds for each server
# socket. Not supported on OS X. (integer value)
#tcp_keepidle=600


#
# Options defined in nova.api.auth
#

# whether to use per-user rate limiting for the api. (boolean
# value)
#api_rate_limit=false

# The strategy to use for auth: noauth or keystone. (string
# value)
#auth_strategy=noauth

# Treat X-Forwarded-For as the canonical remote address. Only
# enable this if you have a sanitizing proxy. (boolean value)
#use_forwarded_for=false


#
# Options defined in nova.api.ec2
#

# Number of failed auths before lockout. (integer value)
#lockout_attempts=5

# Number of minutes to lockout if triggered. (integer value)
#lockout_minutes=15

# Number of minutes for lockout window. (integer value)
#lockout_window=15

# URL to get token from ec2 request. (string value)
#keystone_ec2_url=http://localhost:5000/v2.0/ec2tokens

# Return the IP address as private dns hostname in describe
# instances (boolean value)
#ec2_private_dns_show_ip=false

# Validate security group names according to EC2 specification
# (boolean value)
#ec2_strict_validation=true

# Time in seconds before ec2 timestamp expires (integer value)
#ec2_timestamp_expiry=300


#
# Options defined in nova.api.ec2.cloud
#

# the ip of the ec2 api server (string value)
#ec2_host=$my_ip

# the internal ip of the ec2 api server (string value)
#ec2_dmz_host=$my_ip

# the port of the ec2 api server (integer value)
#ec2_port=8773

# the protocol to use when connecting to the ec2 api server
# (http, https) (string value)
#ec2_scheme=http

# the path prefix used to call the ec2 api server (string
# value)
#ec2_path=/services/Cloud

# list of region=fqdn pairs separated by commas (list value)
#region_list=


#
# Options defined in nova.api.metadata.base
#

# List of metadata versions to skip placing into the config
# drive (string value)
#config_drive_skip_versions=1.0 2007-01-19 2007-03-01 2007-08-29 2007-10-10 2007-12-15 2008-02-01 2008-09-01

# Driver to use for vendor data (string value)
#vendordata_driver=nova.api.metadata.vendordata_json.JsonFileVendorData


#
# Options defined in nova.api.metadata.handler
#

# Set flag to indicate Neutron will proxy metadata requests
# and resolve instance ids. (boolean value)
#service_neutron_metadata_proxy=false

# Shared secret to validate proxies Neutron metadata requests
# (string value)
#neutron_metadata_proxy_shared_secret=


#
# Options defined in nova.api.metadata.vendordata_json
#

# File to load json formated vendor data from (string value)
#vendordata_jsonfile_path=<None>


#
# Options defined in nova.api.openstack.common
#

# the maximum number of items returned in a single response
# from a collection resource (integer value)
#osapi_max_limit=1000

# Base URL that will be presented to users in links to the
# OpenStack Compute API (string value)
#osapi_compute_link_prefix=<None>

# Base URL that will be presented to users in links to glance
# resources (string value)
#osapi_glance_link_prefix=<None>


#
# Options defined in nova.api.openstack.compute
#

# Permit instance snapshot operations. (boolean value)
#allow_instance_snapshots=true


#
# Options defined in nova.api.openstack.compute.contrib
#

# Specify list of extensions to load when using
# osapi_compute_extension option with
# nova.api.openstack.compute.contrib.select_extensions (list
# value)
#osapi_compute_ext_list=


#
# Options defined in nova.api.openstack.compute.contrib.fping
#

# Full path to fping. (string value)
#fping_path=/usr/sbin/fping


#
# Options defined in nova.api.openstack.compute.contrib.os_tenant_networks
#

# Enables or disables quotaing of tenant networks (boolean
# value)
#enable_network_quota=false

# Control for checking for default networks (string value)
#use_neutron_default_nets=False

# Default tenant id when creating neutron networks (string
# value)
#neutron_default_tenant_id=default


#
# Options defined in nova.api.openstack.compute.extensions
#

# osapi compute extension to load (multi valued)
#osapi_compute_extension=nova.api.openstack.compute.contrib.standard_extensions


#
# Options defined in nova.api.openstack.compute.plugins.v3.hide_server_addresses
#

# List of instance states that should hide network info (list
# value)
#osapi_hide_server_address_states=building


#
# Options defined in nova.api.openstack.compute.servers
#

# Allows use of instance password during server creation
# (boolean value)
#enable_instance_password=true


#
# Options defined in nova.api.sizelimit
#

# the maximum body size per each osapi request(bytes) (integer
# value)
#osapi_max_request_body_size=114688


#
# Options defined in nova.cells.opts
#

# The full class name of the compute API class to use
# (deprecated) (string value)
#compute_api_class=nova.compute.api.API


#
# Options defined in nova.cert.rpcapi
#

# the topic cert nodes listen on (string value)
#cert_topic=cert


#
# Options defined in nova.cloudpipe.pipelib
#

# image id used when starting up a cloudpipe vpn server
# (string value)
#vpn_image_id=0

# Flavor for vpn instances (string value)
#vpn_flavor=m1.tiny

# Template for cloudpipe instance boot script (string value)
#boot_script_template=$pybasedir/nova/cloudpipe/bootscript.template

# Network to push into openvpn config (string value)
#dmz_net=10.0.0.0

# Netmask to push into openvpn config (string value)
#dmz_mask=255.255.255.0

# Suffix to add to project name for vpn key and secgroups
# (string value)
#vpn_key_suffix=-vpn


#
# Options defined in nova.cmd.novnc
#

# Record sessions to FILE.[session_number] (boolean value)
#record=false

# Become a daemon (background process) (boolean value)
#daemon=false

# Disallow non-encrypted connections (boolean value)
#ssl_only=false

# Source is ipv6 (boolean value)
#source_is_ipv6=false

# SSL certificate file (string value)
#cert=self.pem

# SSL key file (if separate from cert) (string value)
#key=<None>

# Run webserver on same port. Serve files from DIR. (string
# value)
#web=/usr/share/spice-html5


#
# Options defined in nova.cmd.novncproxy
#

# Host on which to listen for incoming requests (string value)
#novncproxy_host=0.0.0.0

# Port on which to listen for incoming requests (integer
# value)
#novncproxy_port=6080


#
# Options defined in nova.cmd.spicehtml5proxy
#

# Host on which to listen for incoming requests (string value)
#spicehtml5proxy_host=0.0.0.0

# Port on which to listen for incoming requests (integer
# value)
#spicehtml5proxy_port=6082


#
# Options defined in nova.compute.api
#

# Allow destination machine to match source for resize. Useful
# when testing in single-host environments. (boolean value)
#allow_resize_to_same_host=false

# Allow migrate machine to the same host. Useful when testing
# in single-host environments. (boolean value)
#allow_migrate_to_same_host=false

# availability zone to use when user doesn't specify one
# (string value)
#default_schedule_zone=<None>

# These are image properties which a snapshot should not
# inherit from an instance (list value)
#non_inheritable_image_properties=cache_in_nova,bittorrent

# kernel image that indicates not to use a kernel, but to use
# a raw disk image instead (string value)
#null_kernel=nokernel

# When creating multiple instances with a single request using
# the os-multiple-create API extension, this template will be
# used to build the display name for each instance. The
# benefit is that the instances end up with different
# hostnames. To restore legacy behavior of every instance
# having the same name, set this option to "%(name)s".  Valid
# keys for the template are: name, uuid, count. (string value)
#multi_instance_display_name_template=%(name)s-%(uuid)s

# Maximum number of devices that will result in a local image
# being created on the hypervisor node. Setting this to 0
# means nova will allow only boot from volume. A negative
# number means unlimited. (integer value)
#max_local_block_devices=3


#
# Options defined in nova.compute.flavors
#

# default flavor to use for the EC2 API only. The Nova API
# does not support a default flavor. (string value)
#default_flavor=m1.small


#
# Options defined in nova.compute.manager
#

# Console proxy host to use to connect to instances on this
# host. (string value)
#console_host=nova

# Name of network to use to set access ips for instances
# (string value)
#default_access_ip_network_name=<None>

# Whether to batch up the application of IPTables rules during
# a host restart and apply all at the end of the init phase
# (boolean value)
#defer_iptables_apply=false

# where instances are stored on disk (string value)
#instances_path=$state_path/instances

# Generate periodic compute.instance.exists notifications
# (boolean value)
#instance_usage_audit=false

# Number of 1 second retries needed in live_migration (integer
# value)
#live_migration_retry_count=30

# Whether to start guests that were running before the host
# rebooted (boolean value)
#resume_guests_state_on_host_boot=false

# Number of times to retry network allocation on failures
# (integer value)
#network_allocate_retries=0

# The number of times to attempt to reap an instance's files.
# (integer value)
#maximum_instance_delete_attempts=5

# interval to pull bandwidth usage info (integer value)
#bandwidth_poll_interval=600

# interval to sync power states between the database and the
# hypervisor (integer value)
#sync_power_state_interval=600

# Number of seconds between instance info_cache self healing
# updates (integer value)
#heal_instance_info_cache_interval=60

# Interval in seconds for querying the host status (integer
# value)
#host_state_interval=120

# Number of seconds to wait between runs of the image cache
# manager (integer value)
#image_cache_manager_interval=2400

# Interval in seconds for reclaiming deleted instances
# (integer value)
#reclaim_instance_interval=0

# Interval in seconds for gathering volume usages (integer
# value)
#volume_usage_poll_interval=0

# Interval in seconds for polling shelved instances to offload
# (integer value)
#shelved_poll_interval=3600

# Time in seconds before a shelved instance is eligible for
# removing from a host.  -1 never offload, 0 offload when
# shelved (integer value)
#shelved_offload_time=0

# Interval in seconds for retrying failed instance file
# deletes (integer value)
#instance_delete_interval=300

# Action to take if a running deleted instance is
# detected.Valid options are 'noop', 'log' and 'reap'. Set to
# 'noop' to disable. (string value)
#running_deleted_instance_action=log

# Number of seconds to wait between runs of the cleanup task.
# (integer value)
#running_deleted_instance_poll_interval=1800

# Number of seconds after being deleted when a running
# instance should be considered eligible for cleanup. (integer
# value)
#running_deleted_instance_timeout=0

# Automatically hard reboot an instance if it has been stuck
# in a rebooting state longer than N seconds. Set to 0 to
# disable. (integer value)
#reboot_timeout=0

# Amount of time in seconds an instance can be in BUILD before
# going into ERROR status.Set to 0 to disable. (integer value)
#instance_build_timeout=0

# Automatically unrescue an instance after N seconds. Set to 0
# to disable. (integer value)
#rescue_timeout=0

# Automatically confirm resizes after N seconds. Set to 0 to
# disable. (integer value)
#resize_confirm_window=0


#
# Options defined in nova.compute.resource_tracker
#

# Amount of disk in MB to reserve for the host (integer value)
#reserved_host_disk_mb=0

# Amount of memory in MB to reserve for the host (integer
# value)
#reserved_host_memory_mb=512

# Class that will manage stats for the local compute host
# (string value)
#compute_stats_class=nova.compute.stats.Stats


#
# Options defined in nova.compute.rpcapi
#

# the topic compute nodes listen on (string value)
#compute_topic=compute


#
# Options defined in nova.conductor.tasks.live_migrate
#

# Number of times to retry live-migration before failing. If
# == -1, try until out of hosts. If == 0, only try once, no
# retries. (integer value)
#migrate_max_retries=-1


#
# Options defined in nova.console.manager
#

# Driver to use for the console proxy (string value)
#console_driver=nova.console.xvp.XVPConsoleProxy

# Stub calls to compute worker for tests (boolean value)
#stub_compute=false

# Publicly visible name for this console host (string value)
#console_public_hostname=nova


#
# Options defined in nova.console.rpcapi
#

# the topic console proxy nodes listen on (string value)
#console_topic=console


#
# Options defined in nova.console.vmrc
#

# port for VMware VMRC connections (integer value)
#console_vmrc_port=443

# number of retries for retrieving VMRC information (integer
# value)
#console_vmrc_error_retries=10


#
# Options defined in nova.console.xvp
#

# XVP conf template (string value)
#console_xvp_conf_template=$pybasedir/nova/console/xvp.conf.template

# generated XVP conf file (string value)
#console_xvp_conf=/etc/xvp.conf

# XVP master process pid file (string value)
#console_xvp_pid=/var/run/xvp.pid

# XVP log file (string value)
#console_xvp_log=/var/log/xvp.log

# port for XVP to multiplex VNC connections on (integer value)
#console_xvp_multiplex_port=5900


#
# Options defined in nova.consoleauth
#

# the topic console auth proxy nodes listen on (string value)
#consoleauth_topic=consoleauth


#
# Options defined in nova.consoleauth.manager
#

# How many seconds before deleting tokens (integer value)
#console_token_ttl=600

# Manager for console auth (string value)
#consoleauth_manager=nova.consoleauth.manager.ConsoleAuthManager


#
# Options defined in nova.db.api
#

# Services to be added to the available pool on create
# (boolean value)
#enable_new_services=true

# Template string to be used to generate instance names
# (string value)
#instance_name_template=instance-%08x

# Template string to be used to generate snapshot names
# (string value)
#snapshot_name_template=snapshot-%s


#
# Options defined in nova.db.base
#

# driver to use for database access (string value)
#db_driver=nova.db


#
# Options defined in nova.db.sqlalchemy.api
#

# When set, compute API will consider duplicate hostnames
# invalid within the specified scope, regardless of case.
# Should be empty, "project" or "global". (string value)
#osapi_compute_unique_server_name_scope=


#
# Options defined in nova.image.glance
#

# default glance hostname or ip (string value)
#glance_host=$my_ip

# default glance port (integer value)
#glance_port=9292

# Default protocol to use when connecting to glance. Set to
# https for SSL. (string value)
#glance_protocol=http

# A list of the glance api servers available to nova. Prefix
# with https:// for ssl-based glance api servers.
# ([hostname|ip]:port) (list value)
#glance_api_servers=$glance_host:$glance_port

# Allow to perform insecure SSL (https) requests to glance
# (boolean value)
#glance_api_insecure=false

# Number retries when downloading an image from glance
# (integer value)
#glance_num_retries=0

# A list of url scheme that can be downloaded directly via the
# direct_url.  Currently supported schemes: [file]. (list
# value)
#allowed_direct_url_schemes=


#
# Options defined in nova.image.s3
#

# parent dir for tempdir used for image decryption (string
# value)
#image_decryption_dir=/tmp

# hostname or ip for OpenStack to use when accessing the s3
# api (string value)
#s3_host=$my_ip

# port used when accessing the s3 api (integer value)
#s3_port=3333

# access key to use for s3 server for images (string value)
#s3_access_key=notchecked

# secret key to use for s3 server for images (string value)
#s3_secret_key=notchecked

# whether to use ssl when talking to s3 (boolean value)
#s3_use_ssl=false

# whether to affix the tenant id to the access key when
# downloading from s3 (boolean value)
#s3_affix_tenant=false


#
# Options defined in nova.ipv6.api
#

# Backend to use for IPv6 generation (string value)
#ipv6_backend=rfc2462


#
# Options defined in nova.network
#

# The full class name of the network API class to use (string
# value)
#network_api_class=nova.network.api.API


#
# Options defined in nova.network.driver
#

# Driver to use for network creation (string value)
#network_driver=nova.network.linux_net


#
# Options defined in nova.network.floating_ips
#

# Default pool for floating ips (string value)
#default_floating_pool=nova

# Autoassigning floating ip to VM (boolean value)
#auto_assign_floating_ip=false

# full class name for the DNS Manager for floating IPs (string
# value)
#floating_ip_dns_manager=nova.network.noop_dns_driver.NoopDNSDriver

# full class name for the DNS Manager for instance IPs (string
# value)
#instance_dns_manager=nova.network.noop_dns_driver.NoopDNSDriver

# full class name for the DNS Zone for instance IPs (string
# value)
#instance_dns_domain=


#
# Options defined in nova.network.ldapdns
#

# URL for ldap server which will store dns entries (string
# value)
#ldap_dns_url=ldap://ldap.example.com:389

# user for ldap DNS (string value)
#ldap_dns_user=uid=admin,ou=people,dc=example,dc=org

# password for ldap DNS (string value)
#ldap_dns_password=password

# Hostmaster for ldap dns driver Statement of Authority
# (string value)
#ldap_dns_soa_hostmaster=hostmaster@example.org

# DNS Servers for ldap dns driver (multi valued)
#ldap_dns_servers=dns.example.org

# Base DN for DNS entries in ldap (string value)
#ldap_dns_base_dn=ou=hosts,dc=example,dc=org

# Refresh interval (in seconds) for ldap dns driver Statement
# of Authority (string value)
#ldap_dns_soa_refresh=1800

# Retry interval (in seconds) for ldap dns driver Statement of
# Authority (string value)
#ldap_dns_soa_retry=3600

# Expiry interval (in seconds) for ldap dns driver Statement
# of Authority (string value)
#ldap_dns_soa_expiry=86400

# Minimum interval (in seconds) for ldap dns driver Statement
# of Authority (string value)
#ldap_dns_soa_minimum=7200


#
# Options defined in nova.network.linux_net
#

# location of flagfiles for dhcpbridge (multi valued)
#dhcpbridge_flagfile=/etc/nova/nova-dhcpbridge.conf

# Location to keep network config files (string value)
#networks_path=$state_path/networks

# Interface for public IP addresses (string value)
#public_interface=eth0

# MTU setting for vlan (string value)
#network_device_mtu=<None>

# location of nova-dhcpbridge (string value)
#dhcpbridge=$bindir/nova-dhcpbridge

# Public IP of network host (string value)
#routing_source_ip=$my_ip

# Lifetime of a DHCP lease in seconds (integer value)
#dhcp_lease_time=120

# if set, uses specific dns server for dnsmasq. Canbe
# specified multiple times. (multi valued)
#dns_server=

# if set, uses the dns1 and dns2 from the network ref.as dns
# servers. (boolean value)
#use_network_dns_servers=false

# A list of dmz range that should be accepted (list value)
#dmz_cidr=

# Traffic to this range will always be snatted to the fallback
# ip, even if it would normally be bridged out of the node.
# Can be specified multiple times. (multi valued)
#force_snat_range=

# Override the default dnsmasq settings with this file (string
# value)
#dnsmasq_config_file=

# Driver used to create ethernet devices. (string value)
#linuxnet_interface_driver=nova.network.linux_net.LinuxBridgeInterfaceDriver

# Name of Open vSwitch bridge used with linuxnet (string
# value)
#linuxnet_ovs_integration_bridge=br-int

# send gratuitous ARPs for HA setup (boolean value)
#send_arp_for_ha=false

# send this many gratuitous ARPs for HA setup (integer value)
#send_arp_for_ha_count=3

# Use single default gateway. Only first nic of vm will get
# default gateway from dhcp server (boolean value)
#use_single_default_gateway=false

# An interface that bridges can forward to. If this is set to
# all then all traffic will be forwarded. Can be specified
# multiple times. (multi valued)
#forward_bridge_interface=all

# the ip for the metadata api server (string value)
#metadata_host=$my_ip

# the port for the metadata api port (integer value)
#metadata_port=8775

# Regular expression to match iptables rule that shouldalways
# be on the top. (string value)
#iptables_top_regex=

# Regular expression to match iptables rule that shouldalways
# be on the bottom. (string value)
#iptables_bottom_regex=

# The table that iptables to jump to when a packet is to be
# dropped. (string value)
#iptables_drop_action=DROP


#
# Options defined in nova.network.manager
#

# Bridge for simple network instances (string value)
#flat_network_bridge=<None>

# Dns for simple network (string value)
#flat_network_dns=8.8.4.4

# Whether to attempt to inject network setup into guest
# (boolean value)
#flat_injected=false

# FlatDhcp will bridge into this interface if set (string
# value)
#flat_interface=<None>

# First VLAN for private networks (integer value)
#vlan_start=100

# vlans will bridge into this interface if set (string value)
#vlan_interface=<None>

# Number of networks to support (integer value)
#num_networks=1

# Public IP for the cloudpipe VPN servers (string value)
#vpn_ip=$my_ip

# First Vpn port for private networks (integer value)
#vpn_start=1000

# Number of addresses in each private subnet (integer value)
#network_size=256

# Fixed IPv6 address block (string value)
#fixed_range_v6=fd00::/48

# Default IPv4 gateway (string value)
#gateway=<None>

# Default IPv6 gateway (string value)
#gateway_v6=<None>

# Number of addresses reserved for vpn clients (integer value)
#cnt_vpn_clients=0

# Seconds after which a deallocated ip is disassociated
# (integer value)
#fixed_ip_disassociate_timeout=600

# Number of attempts to create unique mac address (integer
# value)
#create_unique_mac_address_attempts=5

# If passed, use fake network devices and addresses (boolean
# value)
#fake_network=false

# If True, skip using the queue and make local calls (boolean
# value)
#fake_call=false

# If True, unused gateway devices (VLAN and bridge) are
# deleted in VLAN network mode with multi hosted networks
# (boolean value)
#teardown_unused_network_gateway=false

# If True, send a dhcp release on instance termination
# (boolean value)
#force_dhcp_release=true

# If True in multi_host mode, all compute hosts share the same
# dhcp address. The same IP address used for DHCP will be
# added on each nova-network node which is only visible to the
# vms on the same host. (boolean value)
#share_dhcp_address=false

# If True, when a DNS entry must be updated, it sends a fanout
# cast to all network hosts to update their DNS entries in
# multi host mode (boolean value)
#update_dns_entries=false

# Number of seconds to wait between runs of updates to DNS
# entries. (integer value)
#dns_update_periodic_interval=-1

# domain to use for building the hostnames (string value)
#dhcp_domain=novalocal

# Indicates underlying L3 management library (string value)
#l3_lib=nova.network.l3.LinuxNetL3


#
# Options defined in nova.network.neutronv2.api
#

# URL for connecting to neutron (string value)
#neutron_url=http://127.0.0.1:9696

# timeout value for connecting to neutron in seconds (integer
# value)
#neutron_url_timeout=30

# username for connecting to neutron in admin context (string
# value)
#neutron_admin_username=<None>

# password for connecting to neutron in admin context (string
# value)
#neutron_admin_password=<None>

# tenant name for connecting to neutron in admin context
# (string value)
#neutron_admin_tenant_name=<None>

# region name for connecting to neutron in admin context
# (string value)
#neutron_region_name=<None>

# auth url for connecting to neutron in admin context (string
# value)
#neutron_admin_auth_url=http://localhost:5000/v2.0

# if set, ignore any SSL validation issues (boolean value)
#neutron_api_insecure=false

# auth strategy for connecting to neutron in admin context
# (string value)
#neutron_auth_strategy=keystone

# Name of Integration Bridge used by Open vSwitch (string
# value)
#neutron_ovs_bridge=br-int

# Number of seconds before querying neutron for extensions
# (integer value)
#neutron_extension_sync_interval=600

# Location of ca certicates file to use for neutronclient
# requests. (string value)
#neutron_ca_certificates_file=<None>

# Use per-port DHCP options with Neutron (boolean value)
#dhcp_options_enabled=false


#
# Options defined in nova.network.rpcapi
#

# the topic network nodes listen on (string value)
#network_topic=network

# Default value for multi_host in networks. Also, if set, some
# rpc network calls will be sent directly to host. (boolean
# value)
#multi_host=false


#
# Options defined in nova.network.security_group.openstack_driver
#

# The full class name of the security API class (string value)
#security_group_api=nova


#
# Options defined in nova.objectstore.s3server
#

# path to s3 buckets (string value)
#buckets_path=$state_path/buckets

# IP address for S3 API to listen (string value)
#s3_listen=0.0.0.0

# port for s3 api to listen (integer value)
#s3_listen_port=3333


#
# Options defined in nova.openstack.common.db.sqlalchemy.session
#

# the filename to use with sqlite (string value)
#sqlite_db=nova.sqlite

# If true, use synchronous mode for sqlite (boolean value)
#sqlite_synchronous=true


#
# Options defined in nova.openstack.common.eventlet_backdoor
#

# Enable eventlet backdoor. Acceptable values are 0, <port>
# and <start>:<end>, where 0 results in listening on a random
# tcp port number, <port> results in listening on the
# specified port number and not enabling backdoorif it is in
# use and <start>:<end> results in listening on the smallest
# unused port number within the specified range of port
# numbers. The chosen port is displayed in the service's log
# file. (string value)
#backdoor_port=<None>


#
# Options defined in nova.openstack.common.lockutils
#

# Whether to disable inter-process locks (boolean value)
#disable_process_locking=false

# Directory to use for lock files. (string value)
#lock_path=<None>


#
# Options defined in nova.openstack.common.log
#

# Print debugging output (set logging level to DEBUG instead
# of default WARNING level). (boolean value)
#debug=false

# Print more verbose output (set logging level to INFO instead
# of default WARNING level). (boolean value)
#verbose=false
nova.param('verbose', type='boolean', default=False, description='Print more verbose output (set logging level to INFO instead of default WARNING level)')

# Log output to standard error (boolean value)
#use_stderr=true
nova.param('use_stderr', type='boolean', default=True, description='Log output to standard error')

# format string to use for log messages with context (string
# value)
#logging_context_format_string=%(asctime)s.%(msecs)03d %(process)d %(levelname)s %(name)s [%(request_id)s %(user)s %(tenant)s] %(instance)s%(message)s

# format string to use for log messages without context
# (string value)
#logging_default_format_string=%(asctime)s.%(msecs)03d %(process)d %(levelname)s %(name)s [-] %(instance)s%(message)s

# data to append to log format when level is DEBUG (string
# value)
#logging_debug_format_suffix=%(funcName)s %(pathname)s:%(lineno)d

# prefix each line of exception output with this format
# (string value)
#logging_exception_prefix=%(asctime)s.%(msecs)03d %(process)d TRACE %(name)s %(instance)s

# list of logger=LEVEL pairs (list value)
#default_log_levels=amqplib=WARN,sqlalchemy=WARN,boto=WARN,suds=INFO,keystone=INFO,eventlet.wsgi.server=WARN

# publish error events (boolean value)
#publish_errors=false

# make deprecations fatal (boolean value)
#fatal_deprecations=false

# If an instance is passed with the log message, format it
# like this (string value)
#instance_format="[instance: %(uuid)s] "

# If an instance UUID is passed with the log message, format
# it like this (string value)
#instance_uuid_format="[instance: %(uuid)s] "

# If this option is specified, the logging configuration file
# specified is used and overrides any other logging options
# specified. Please see the Python logging module
# documentation for details on logging configuration files.
# (string value)
#log_config=<None>

# DEPRECATED. A logging.Formatter log message format string
# which may use any of the available logging.LogRecord
# attributes. This option is deprecated.  Please use
# logging_context_format_string and
# logging_default_format_string instead. (string value)
#log_format=<None>

# Format string for %%(asctime)s in log records. Default:
# %(default)s (string value)
#log_date_format=%Y-%m-%d %H:%M:%S

# (Optional) Name of log file to output to. If no default is
# set, logging will go to stdout. (string value)
#log_file=<None>

# (Optional) The base directory used for relative --log-file
# paths (string value)
#log_dir=<None>

# Use syslog for logging. (boolean value)
#use_syslog=false

# syslog facility to receive log lines (string value)
#syslog_log_facility=LOG_USER


#
# Options defined in nova.openstack.common.memorycache
#

# Memcached servers or None for in process cache. (list value)
#memcached_servers=<None>


#
# Options defined in nova.openstack.common.notifier.api
#

# Driver or drivers to handle sending notifications (multi
# valued)
#notification_driver=

# Default notification level for outgoing notifications
# (string value)
#default_notification_level=INFO

# Default publisher_id for outgoing notifications (string
# value)
#default_publisher_id=<None>


#
# Options defined in nova.openstack.common.notifier.rpc_notifier
#

# AMQP topic used for OpenStack notifications (list value)
#notification_topics=notifications


#
# Options defined in nova.openstack.common.periodic_task
#

# Some periodic tasks can be run in a separate process. Should
# we run them here? (boolean value)
#run_external_periodic_tasks=true


#
# Options defined in nova.openstack.common.rpc
#

# The messaging module to use, defaults to kombu. (string
# value)
#rpc_backend=nova.openstack.common.rpc.impl_kombu

# Size of RPC thread pool (integer value)
#rpc_thread_pool_size=64

# Size of RPC connection pool (integer value)
#rpc_conn_pool_size=30

# Seconds to wait for a response from call or multicall
# (integer value)
#rpc_response_timeout=60

# Seconds to wait before a cast expires (TTL). Only supported
# by impl_zmq. (integer value)
#rpc_cast_timeout=30

# Modules of exceptions that are permitted to be recreatedupon
# receiving exception data from an rpc call. (list value)
#allowed_rpc_exception_modules=nova.exception,cinder.exception,exceptions

# If passed, use a fake RabbitMQ provider (boolean value)
#fake_rabbit=false

# AMQP exchange to connect to if using RabbitMQ or Qpid
# (string value)
#control_exchange=openstack


#
# Options defined in nova.openstack.common.rpc.amqp
#

# Use durable queues in amqp. (boolean value)
#amqp_durable_queues=false

# Auto-delete queues in amqp. (boolean value)
#amqp_auto_delete=false
nova.param('amqp_auto_delete', type='boolean')


#
# Options defined in nova.openstack.common.rpc.impl_kombu
#

# SSL version to use (valid only if SSL enabled). valid values
# are TLSv1, SSLv23 and SSLv3. SSLv2 may be available on some
# distributions (string value)
#kombu_ssl_version=

# SSL key file (valid only if SSL enabled) (string value)
#kombu_ssl_keyfile=

# SSL cert file (valid only if SSL enabled) (string value)
#kombu_ssl_certfile=

# SSL certification authority file (valid only if SSL enabled)
# (string value)
#kombu_ssl_ca_certs=

# The RabbitMQ broker address where a single node is used
# (string value)
#rabbit_host=localhost

# The RabbitMQ broker port where a single node is used
# (integer value)
#rabbit_port=5672

nova.param('rabbit_host', type='host')
nova.param('rabbit_port', type='port')

# RabbitMQ HA cluster host:port pairs (list value)
#rabbit_hosts=$rabbit_host:$rabbit_port

# connect over SSL for RabbitMQ (boolean value)
#rabbit_use_ssl=false
nova.param('rabbit_use_ssl', type='boolean', default=False)

# the RabbitMQ userid (string value)
#rabbit_userid=guest
nova.param('rabbit_userid', type='string', default='guest')

# the RabbitMQ password (string value)
#rabbit_password=guest
nova.param('rabbit_password', type='string', default='guest')

# the RabbitMQ virtual host (string value)
#rabbit_virtual_host=/
nova.param('rabbit_virtual_host', type='string', default='/')

# how frequently to retry connecting with RabbitMQ (integer
# value)
#rabbit_retry_interval=1
nova.param('rabbit_retry_interval', type='integer', default=1)

# how long to backoff for between retries when connecting to
# RabbitMQ (integer value)
#rabbit_retry_backoff=2

# maximum retries with trying to connect to RabbitMQ (the
# default of 0 implies an infinite retry count) (integer
# value)
#rabbit_max_retries=0

# use H/A queues in RabbitMQ (x-ha-policy: all).You need to
# wipe RabbitMQ database when changing this option. (boolean
# value)
#rabbit_ha_queues=false


#
# Options defined in nova.openstack.common.rpc.impl_qpid
#

# Qpid broker hostname (string value)
#qpid_hostname=localhost

# Qpid broker port (integer value)
#qpid_port=5672

# Qpid HA cluster host:port pairs (list value)
#qpid_hosts=$qpid_hostname:$qpid_port

# Username for qpid connection (string value)
#qpid_username=

# Password for qpid connection (string value)
#qpid_password=

# Space separated list of SASL mechanisms to use for auth
# (string value)
#qpid_sasl_mechanisms=

# Seconds between connection keepalive heartbeats (integer
# value)
#qpid_heartbeat=60

# Transport to use, either 'tcp' or 'ssl' (string value)
#qpid_protocol=tcp

# Disable Nagle algorithm (boolean value)
#qpid_tcp_nodelay=true

# The qpid topology version to use.  Version 1 is what was
# originally used by impl_qpid.  Version 2 includes some
# backwards-incompatible changes that allow broker federation
# to work.  Users should update to version 2 when they are
# able to take everything down, as it requires a clean break.
# (integer value)
#qpid_topology_version=1


#
# Options defined in nova.openstack.common.rpc.impl_zmq
#

# ZeroMQ bind address. Should be a wildcard (*), an ethernet
# interface, or IP. The "host" option should point or resolve
# to this address. (string value)
#rpc_zmq_bind_address=*

# MatchMaker driver (string value)
#rpc_zmq_matchmaker=nova.openstack.common.rpc.matchmaker.MatchMakerLocalhost

# ZeroMQ receiver listening port (integer value)
#rpc_zmq_port=9501

# Number of ZeroMQ contexts, defaults to 1 (integer value)
#rpc_zmq_contexts=1

# Maximum number of ingress messages to locally buffer per
# topic. Default is unlimited. (integer value)
#rpc_zmq_topic_backlog=<None>

# Directory for holding IPC sockets (string value)
#rpc_zmq_ipc_dir=/var/run/openstack

# Name of this node. Must be a valid hostname, FQDN, or IP
# address. Must match "host" option, if running Nova. (string
# value)
#rpc_zmq_host=nova


#
# Options defined in nova.openstack.common.rpc.matchmaker
#

# Heartbeat frequency (integer value)
#matchmaker_heartbeat_freq=300

# Heartbeat time-to-live. (integer value)
#matchmaker_heartbeat_ttl=600


#
# Options defined in nova.pci.pci_request
#

# An alias for a PCI passthrough device requirement. This
# allows users to specify the alias in the extra_spec for a
# flavor, without needing to repeat all the PCI property
# requirements. For example: pci_alias = { "name":
# "QuicAssist",   "product_id": "0443",   "vendor_id": "8086",
# "device_type": "ACCEL" } defines an alias for the Intel
# QuickAssist card. (multi valued) (multi valued)
#pci_alias=


#
# Options defined in nova.pci.pci_whitelist
#

# White list of PCI devices available to VMs. For example:
# pci_passthrough_whitelist =  [{"vendor_id": "8086",
# "product_id": "0443"}] (multi valued)
#pci_passthrough_whitelist=


#
# Options defined in nova.scheduler.driver
#

# The scheduler host manager class to use (string value)
#scheduler_host_manager=nova.scheduler.host_manager.HostManager

# Maximum number of attempts to schedule an instance (integer
# value)
#scheduler_max_attempts=3


#
# Options defined in nova.scheduler.filter_scheduler
#

# New instances will be scheduled on a host chosen randomly
# from a subset of the N best hosts. This property defines the
# subset size that a host is chosen from. A value of 1 chooses
# the first host returned by the weighing functions. This
# value must be at least 1. Any value less than 1 will be
# ignored, and 1 will be used instead (integer value)
#scheduler_host_subset_size=1


#
# Options defined in nova.scheduler.filters.core_filter
#

# Virtual CPU to physical CPU allocation ratio which affects
# all CPU filters. This configuration specifies a global ratio
# for CoreFilter. For AggregateCoreFilter, it will fall back
# to this configuration value if no per-aggregate setting
# found. (floating point value)
#cpu_allocation_ratio=16.0


#
# Options defined in nova.scheduler.filters.disk_filter
#

# virtual disk to physical disk allocation ratio (floating
# point value)
#disk_allocation_ratio=1.0


#
# Options defined in nova.scheduler.filters.io_ops_filter
#

# Ignore hosts that have too many
# builds/resizes/snaps/migrations (integer value)
#max_io_ops_per_host=8


#
# Options defined in nova.scheduler.filters.isolated_hosts_filter
#

# Images to run on isolated host (list value)
#isolated_images=

# Host reserved for specific images (list value)
#isolated_hosts=

# Whether to force isolated hosts to run only isolated images
# (boolean value)
#restrict_isolated_hosts_to_isolated_images=true


#
# Options defined in nova.scheduler.filters.num_instances_filter
#

# Ignore hosts that have too many instances (integer value)
#max_instances_per_host=50


#
# Options defined in nova.scheduler.filters.ram_filter
#

# Virtual ram to physical ram allocation ratio which affects
# all ram filters. This configuration specifies a global ratio
# for RamFilter. For AggregateRamFilter, it will fall back to
# this configuration value if no per-aggregate setting found.
# (floating point value)
#ram_allocation_ratio=1.5


#
# Options defined in nova.scheduler.host_manager
#

# Filter classes available to the scheduler which may be
# specified more than once.  An entry of
# "nova.scheduler.filters.standard_filters" maps to all
# filters included with nova. (multi valued)
#scheduler_available_filters=nova.scheduler.filters.all_filters

# Which filter class names to use for filtering hosts when not
# specified in the request. (list value)
#scheduler_default_filters=RetryFilter,AvailabilityZoneFilter,RamFilter,ComputeFilter,ComputeCapabilitiesFilter,ImagePropertiesFilter

# Which weight class names to use for weighing hosts (list
# value)
#scheduler_weight_classes=nova.scheduler.weights.all_weighers


#
# Options defined in nova.scheduler.manager
#

# Default driver to use for the scheduler (string value)
#scheduler_driver=nova.scheduler.filter_scheduler.FilterScheduler


#
# Options defined in nova.scheduler.rpcapi
#

# the topic scheduler nodes listen on (string value)
#scheduler_topic=scheduler


#
# Options defined in nova.scheduler.scheduler_options
#

# Absolute path to scheduler configuration JSON file. (string
# value)
#scheduler_json_config_location=


#
# Options defined in nova.scheduler.weights.ram
#

# Multiplier used for weighing ram.  Negative numbers mean to
# stack vs spread. (floating point value)
#ram_weight_multiplier=1.0


#
# Options defined in nova.servicegroup.api
#

# The driver for servicegroup service (valid options are: db,
# zk, mc) (string value)
#servicegroup_driver=db


#
# Options defined in nova.virt.configdrive
#

# Config drive format. One of iso9660 (default) or vfat
# (string value)
#config_drive_format=iso9660

# Where to put temporary files associated with config drive
# creation (string value)
#config_drive_tempdir=<None>

# Set to force injection to take place on a config drive (if
# set, valid options are: always) (string value)
#force_config_drive=<None>

# Name and optionally path of the tool used for ISO image
# creation (string value)
#mkisofs_cmd=genisoimage


#
# Options defined in nova.virt.disk.api
#

# Template file for injected network (string value)
#injected_network_template=$pybasedir/nova/virt/interfaces.template

# mkfs commands for ephemeral device. The format is
# <os_type>=<mkfs command> (multi valued)
#virt_mkfs=default=mkfs.ext3 -L %(fs_label)s -F %(target)s
#virt_mkfs=linux=mkfs.ext3 -L %(fs_label)s -F %(target)s
#virt_mkfs=windows=mkfs.ntfs --force --fast --label %(fs_label)s %(target)s

# Attempt to resize the filesystem by accessing the image over
# a block device. This is done by the host and may not be
# necessary if the image contains a recent version of cloud-
# init. Possible mechanisms require the nbd driver (for qcow
# and raw), or loop (for raw). (boolean value)
#resize_fs_using_block_device=true


#
# Options defined in nova.virt.disk.mount.nbd
#

# time to wait for a NBD device coming up (integer value)
#timeout_nbd=10


#
# Options defined in nova.virt.docker.driver
#

# Default TCP port to find the docker-registry container
# (integer value)
#docker_registry_default_port=5042


#
# Options defined in nova.virt.driver
#

# Driver to use for controlling virtualization. Options
# include: libvirt.LibvirtDriver, xenapi.XenAPIDriver,
# fake.FakeDriver, baremetal.BareMetalDriver,
# vmwareapi.VMwareESXDriver, vmwareapi.VMwareVCDriver (string
# value)
#compute_driver=<None>

# The default format an ephemeral_volume will be formatted
# with on creation. (string value)
#default_ephemeral_format=<None>

# VM image preallocation mode: "none" => no storage
# provisioning is done up front, "space" => storage is fully
# allocated at instance start (string value)
#preallocate_images=none

# Whether to use cow images (boolean value)
#use_cow_images=true


#
# Options defined in nova.virt.firewall
#

# Firewall driver (defaults to hypervisor specific iptables
# driver) (string value)
#firewall_driver=<None>

# Whether to allow network traffic from same network (boolean
# value)
#allow_same_net_traffic=true


#
# Options defined in nova.virt.images
#

# Force backing images to raw format (boolean value)
#force_raw_images=true


#
# Options defined in nova.virt.libvirt.driver
#

# Rescue ami image (string value)
#rescue_image_id=<None>

# Rescue aki image (string value)
#rescue_kernel_id=<None>

# Rescue ari image (string value)
#rescue_ramdisk_id=<None>

# Libvirt domain type (valid options are: kvm, lxc, qemu, uml,
# xen) (string value)
#libvirt_type=kvm

# Override the default libvirt URI (which is dependent on
# libvirt_type) (string value)
#libvirt_uri=

# Inject the admin password at boot time, without an agent.
# (boolean value)
#libvirt_inject_password=false

# Inject the ssh public key at boot time (boolean value)
#libvirt_inject_key=true

# The partition to inject to : -2 => disable, -1 => inspect
# (libguestfs only), 0 => not partitioned, >0 => partition
# number (integer value)
#libvirt_inject_partition=1

# Sync virtual and real mouse cursors in Windows VMs (boolean
# value)
#use_usb_tablet=true

# Migration target URI (any included "%s" is replaced with the
# migration target hostname) (string value)
#live_migration_uri=qemu+tcp://%s/system

# Migration flags to be set for live migration (string value)
#live_migration_flag=VIR_MIGRATE_UNDEFINE_SOURCE, VIR_MIGRATE_PEER2PEER

# Migration flags to be set for block migration (string value)
#block_migration_flag=VIR_MIGRATE_UNDEFINE_SOURCE, VIR_MIGRATE_PEER2PEER, VIR_MIGRATE_NON_SHARED_INC

# Maximum bandwidth to be used during migration, in Mbps
# (integer value)
#live_migration_bandwidth=0

# Snapshot image format (valid options are : raw, qcow2, vmdk,
# vdi). Defaults to same as source image (string value)
#snapshot_image_format=<None>

# The libvirt VIF driver to configure the VIFs. (string value)
#libvirt_vif_driver=nova.virt.libvirt.vif.LibvirtGenericVIFDriver

# Libvirt handlers for remote volumes. (list value)
#libvirt_volume_drivers=iscsi=nova.virt.libvirt.volume.LibvirtISCSIVolumeDriver,iser=nova.virt.libvirt.volume.LibvirtISERVolumeDriver,local=nova.virt.libvirt.volume.LibvirtVolumeDriver,fake=nova.virt.libvirt.volume.LibvirtFakeVolumeDriver,rbd=nova.virt.libvirt.volume.LibvirtNetVolumeDriver,sheepdog=nova.virt.libvirt.volume.LibvirtNetVolumeDriver,nfs=nova.virt.libvirt.volume.LibvirtNFSVolumeDriver,aoe=nova.virt.libvirt.volume.LibvirtAOEVolumeDriver,glusterfs=nova.virt.libvirt.volume.LibvirtGlusterfsVolumeDriver,fibre_channel=nova.virt.libvirt.volume.LibvirtFibreChannelVolumeDriver,scality=nova.virt.libvirt.volume.LibvirtScalityVolumeDriver

# Override the default disk prefix for the devices attached to
# a server, which is dependent on libvirt_type. (valid options
# are: sd, xvd, uvd, vd) (string value)
#libvirt_disk_prefix=<None>

# Number of seconds to wait for instance to shut down after
# soft reboot request is made. We fall back to hard reboot if
# instance does not shutdown within this window. (integer
# value)
#libvirt_wait_soft_reboot_seconds=120

# Use a separated OS thread pool to realize non-blocking
# libvirt calls (boolean value)
#libvirt_nonblocking=true

# Set to "host-model" to clone the host CPU feature flags; to
# "host-passthrough" to use the host CPU model exactly; to
# "custom" to use a named CPU model; to "none" to not set any
# CPU model. If libvirt_type="kvm|qemu", it will default to
# "host-model", otherwise it will default to "none" (string
# value)
#libvirt_cpu_mode=<None>

# Set to a named libvirt CPU model (see names listed in
# /usr/share/libvirt/cpu_map.xml). Only has effect if
# libvirt_cpu_mode="custom" and libvirt_type="kvm|qemu"
# (string value)
#libvirt_cpu_model=<None>

# Location where libvirt driver will store snapshots before
# uploading them to image service (string value)
#libvirt_snapshots_directory=$instances_path/snapshots

# Location where the Xen hvmloader is kept (string value)
#xen_hvmloader_path=/usr/lib/xen/boot/hvmloader

# Specific cachemodes to use for different disk types e.g:
# ["file=directsync","block=none"] (list value)
#disk_cachemodes=

# Which pcpus can be used by vcpus of instance e.g:
# "4-12,^8,15" (string value)
#vcpu_pin_set=<None>


#
# Options defined in nova.virt.libvirt.imagebackend
#

# VM Images format. Acceptable values are: raw, qcow2,
# lvm,rbd, default. If default is specified, then
# use_cow_images flag is used instead of this one. (string
# value)
#libvirt_images_type=default

# LVM Volume Group that is used for VM images, when you
# specify libvirt_images_type=lvm. (string value)
#libvirt_images_volume_group=<None>

# Create sparse logical volumes (with virtualsize) if this
# flag is set to True. (boolean value)
#libvirt_sparse_logical_volumes=false

# The amount of storage (in megabytes) to allocate for LVM
# snapshot copy-on-write blocks. (integer value)
#libvirt_lvm_snapshot_size=1000

# the RADOS pool in which rbd volumes are stored (string
# value)
#libvirt_images_rbd_pool=rbd

# path to the ceph configuration file to use (string value)
#libvirt_images_rbd_ceph_conf=


#
# Options defined in nova.virt.libvirt.imagecache
#

# Where cached images are stored under $instances_path.This is
# NOT the full path - just a folder name.For per-compute-host
# cached images, set to _base_$my_ip (string value)
#base_dir_name=_base

# Allows image information files to be stored in non-standard
# locations (string value)
#image_info_filename_pattern=$instances_path/$base_dir_name/%(image)s.info

# Should unused base images be removed? (boolean value)
#remove_unused_base_images=true

# Should unused kernel images be removed? This is only safe to
# enable if all compute nodes have been updated to support
# this option. This will enabled by default in future.
# (boolean value)
#remove_unused_kernels=false

# Unused resized base images younger than this will not be
# removed (integer value)
#remove_unused_resized_minimum_age_seconds=3600

# Unused unresized base images younger than this will not be
# removed (integer value)
#remove_unused_original_minimum_age_seconds=86400

# Write a checksum for files in _base to disk (boolean value)
#checksum_base_images=false

# How frequently to checksum base images (integer value)
#checksum_interval_seconds=3600


#
# Options defined in nova.virt.libvirt.utils
#

# Compress snapshot images when possible. This currently
# applies exclusively to qcow2 images (boolean value)
#libvirt_snapshot_compression=false


#
# Options defined in nova.virt.libvirt.vif
#

# Name of Integration Bridge used by Open vSwitch (string
# value)
#libvirt_ovs_bridge=br-int

# Use virtio for bridge interfaces with KVM/QEMU (boolean
# value)
#libvirt_use_virtio_for_bridges=true


#
# Options defined in nova.virt.libvirt.volume
#

# number of times to rescan iSCSI target to find volume
# (integer value)
#num_iscsi_scan_tries=3

# number of times to rescan iSER target to find volume
# (integer value)
#num_iser_scan_tries=3

# the RADOS client name for accessing rbd volumes (string
# value)
#rbd_user=<None>

# the libvirt uuid of the secret for the rbd_uservolumes
# (string value)
#rbd_secret_uuid=<None>

# Dir where the nfs volume is mounted on the compute node
# (string value)
#nfs_mount_point_base=$state_path/mnt

# Mount options passed to the nfs client. See section of the
# nfs man page for details (string value)
#nfs_mount_options=<None>

# number of times to rediscover AoE target to find volume
# (integer value)
#num_aoe_discover_tries=3

# Dir where the glusterfs volume is mounted on the compute
# node (string value)
#glusterfs_mount_point_base=$state_path/mnt

# use multipath connection of the iSCSI volume (boolean value)
#libvirt_iscsi_use_multipath=false

# use multipath connection of the iSER volume (boolean value)
#libvirt_iser_use_multipath=false

# Path or URL to Scality SOFS configuration file (string
# value)
#scality_sofs_config=<None>

# Base dir where Scality SOFS shall be mounted (string value)
#scality_sofs_mount_point=$state_path/scality

# Protocols listed here will be accessed directly from QEMU.
# Currently supported protocols: [gluster] (list value)
#qemu_allowed_storage_drivers=


#
# Options defined in nova.virt.powervm.driver
#

# PowerVM manager type (ivm, hmc) (string value)
#powervm_mgr_type=ivm

# PowerVM manager host or ip (string value)
#powervm_mgr=<None>

# PowerVM manager user name (string value)
#powervm_mgr_user=<None>

# PowerVM manager user password (string value)
#powervm_mgr_passwd=<None>

# PowerVM image remote path where images will be moved. Make
# sure this path can fit your biggest image in glance (string
# value)
#powervm_img_remote_path=/home/padmin

# Local directory to download glance images to. Make sure this
# path can fit your biggest image in glance (string value)
#powervm_img_local_path=/tmp


#
# Options defined in nova.virt.xenapi.agent
#

# number of seconds to wait for agent reply (integer value)
#agent_timeout=30

# number of seconds to wait for agent to be fully operational
# (integer value)
#agent_version_timeout=300

# number of seconds to wait for agent reply to resetnetwork
# request (integer value)
#agent_resetnetwork_timeout=60

# Specifies the path in which the xenapi guest agent should be
# located. If the agent is present, network configuration is
# not injected into the image. Used if
# compute_driver=xenapi.XenAPIDriver and  flat_injected=True
# (string value)
#xenapi_agent_path=usr/sbin/xe-update-networking

# Disables the use of the XenAPI agent in any image regardless
# of what image properties are present.  (boolean value)
#xenapi_disable_agent=false

# Determines if the xenapi agent should be used when the image
# used does not contain a hint to declare if the agent is
# present or not. The hint is a glance property
# "xenapi_use_agent" that has the value "true" or "false".
# Note that waiting for the agent when it is not present will
# significantly increase server boot times. (boolean value)
#xenapi_use_agent_default=false


#
# Options defined in nova.virt.xenapi.driver
#

# URL for connection to XenServer/Xen Cloud Platform. A
# special value of unix://local can be used to connect to the
# local unix socket.  Required if
# compute_driver=xenapi.XenAPIDriver (string value)
#xenapi_connection_url=<None>

# Username for connection to XenServer/Xen Cloud Platform.
# Used only if compute_driver=xenapi.XenAPIDriver (string
# value)
#xenapi_connection_username=root

# Password for connection to XenServer/Xen Cloud Platform.
# Used only if compute_driver=xenapi.XenAPIDriver (string
# value)
#xenapi_connection_password=<None>

# Maximum number of concurrent XenAPI connections. Used only
# if compute_driver=xenapi.XenAPIDriver (integer value)
#xenapi_connection_concurrent=5

# The interval used for polling of coalescing vhds. Used only
# if compute_driver=xenapi.XenAPIDriver (floating point value)
#xenapi_vhd_coalesce_poll_interval=5.0

# Ensure compute service is running on host XenAPI connects
# to. (boolean value)
#xenapi_check_host=true

# Max number of times to poll for VHD to coalesce. Used only
# if compute_driver=xenapi.XenAPIDriver (integer value)
#xenapi_vhd_coalesce_max_attempts=5

# Base path to the storage repository (string value)
#xenapi_sr_base_path=/var/run/sr-mount

# iSCSI Target Host (string value)
#target_host=<None>

# iSCSI Target Port, 3260 Default (string value)
#target_port=3260

# IQN Prefix (string value)
#iqn_prefix=iqn.2010-10.org.openstack

# Used to enable the remapping of VBD dev (Works around an
# issue in Ubuntu Maverick) (boolean value)
#xenapi_remap_vbd_dev=false

# Specify prefix to remap VBD dev to (ex. /dev/xvdb ->
# /dev/sdb) (string value)
#xenapi_remap_vbd_dev_prefix=sd

# Timeout in seconds for XenAPI login. (integer value)
#xenapi_login_timeout=10


#
# Options defined in nova.virt.xenapi.image.bittorrent
#

# Base URL for torrent files. (string value)
#xenapi_torrent_base_url=<None>

# Probability that peer will become a seeder. (1.0 = 100%)
# (floating point value)
#xenapi_torrent_seed_chance=1.0

# Number of seconds after downloading an image via BitTorrent
# that it should be seeded for other peers. (integer value)
#xenapi_torrent_seed_duration=3600

# Cached torrent files not accessed within this number of
# seconds can be reaped (integer value)
#xenapi_torrent_max_last_accessed=86400

# Beginning of port range to listen on (integer value)
#xenapi_torrent_listen_port_start=6881

# End of port range to listen on (integer value)
#xenapi_torrent_listen_port_end=6891

# Number of seconds a download can remain at the same progress
# percentage w/o being considered a stall (integer value)
#xenapi_torrent_download_stall_cutoff=600

# Maximum number of seeder processes to run concurrently
# within a given dom0. (-1 = no limit) (integer value)
#xenapi_torrent_max_seeder_processes_per_host=1


#
# Options defined in nova.virt.xenapi.pool
#

# To use for hosts with different CPUs (boolean value)
#use_join_force=true


#
# Options defined in nova.virt.xenapi.vif
#

# Name of Integration Bridge used by Open vSwitch (string
# value)
#xenapi_ovs_integration_bridge=xapi1


#
# Options defined in nova.virt.xenapi.vm_utils
#

# Cache glance images locally. `all` will cache all images,
# `some` will only cache images that have the image_property
# `cache_in_nova=True`, and `none` turns off caching entirely
# (string value)
#cache_images=all

# Compression level for images, e.g., 9 for gzip -9. Range is
# 1-9, 9 being most compressed but most CPU intensive on dom0.
# (integer value)
#xenapi_image_compression_level=<None>

# Default OS type (string value)
#default_os_type=linux

# Time to wait for a block device to be created (integer
# value)
#block_device_creation_timeout=10

# Maximum size in bytes of kernel or ramdisk images (integer
# value)
#max_kernel_ramdisk_size=16777216

# Filter for finding the SR to be used to install guest
# instances on. To use the Local Storage in default
# XenServer/XCP installations set this flag to other-config
# :i18n-key=local-storage. To select an SR with a different
# matching criteria, you could set it to other-
# config:my_favorite_sr=true. On the other hand, to fall back
# on the Default SR, as displayed by XenCenter, set this flag
# to: default-sr:true (string value)
#sr_matching_filter=default-sr:true

# Whether to use sparse_copy for copying data on a resize down
# (False will use standard dd). This speeds up resizes down
# considerably since large runs of zeros won't have to be
# rsynced (boolean value)
#xenapi_sparse_copy=true

# Maximum number of retries to unplug VBD (integer value)
#xenapi_num_vbd_unplug_retries=10

# Whether or not to download images via Bit Torrent
# (all|some|none). (string value)
#xenapi_torrent_images=none

# Name of network to use for booting iPXE ISOs (string value)
#xenapi_ipxe_network_name=<None>

# URL to the iPXE boot menu (string value)
#xenapi_ipxe_boot_menu_url=<None>

# Name and optionally path of the tool used for ISO image
# creation (string value)
#xenapi_ipxe_mkisofs_cmd=mkisofs


#
# Options defined in nova.virt.xenapi.vmops
#

# number of seconds to wait for instance to go to running
# state (integer value)
#xenapi_running_timeout=60

# The XenAPI VIF driver using XenServer Network APIs. (string
# value)
#xenapi_vif_driver=nova.virt.xenapi.vif.XenAPIBridgeDriver

# Dom0 plugin driver used to handle image uploads. (string
# value)
#xenapi_image_upload_handler=nova.virt.xenapi.image.glance.GlanceStore


#
# Options defined in nova.vnc
#

# location of vnc console proxy, in the form
# "http://127.0.0.1:6080/vnc_auto.html" (string value)
#novncproxy_base_url=http://127.0.0.1:6080/vnc_auto.html

# location of nova xvp vnc console proxy, in the form
# "http://127.0.0.1:6081/console" (string value)
#xvpvncproxy_base_url=http://127.0.0.1:6081/console

# IP address on which instance vncservers should listen
# (string value)
#vncserver_listen=127.0.0.1

# the address to which proxy clients (like nova-xvpvncproxy)
# should connect (string value)
#vncserver_proxyclient_address=127.0.0.1

# enable vnc related features (boolean value)
#vnc_enabled=true

# keymap for vnc (string value)
#vnc_keymap=en-us


#
# Options defined in nova.vnc.xvp_proxy
#

# Port that the XCP VNC proxy should bind to (integer value)
#xvpvncproxy_port=6081

# Address that the XCP VNC proxy should bind to (string value)
#xvpvncproxy_host=0.0.0.0


#
# Options defined in nova.volume
#

# The full class name of the volume API class to use (string
# value)
#volume_api_class=nova.volume.cinder.API


#
# Options defined in nova.volume.cinder
#

# Info to match when looking for cinder in the service
# catalog. Format is : separated values of the form:
# <service_type>:<service_name>:<endpoint_type> (string value)
#cinder_catalog_info=volume:cinder:publicURL

# Override service catalog lookup with template for cinder
# endpoint e.g. http://localhost:8776/v1/%(project_id)s
# (string value)
#cinder_endpoint_template=<None>

# region name of this node (string value)
#os_region_name=<None>

# Location of ca certicates file to use for cinder client
# requests. (string value)
#cinder_ca_certificates_file=<None>

# Number of cinderclient retries on failed http calls (integer
# value)
#cinder_http_retries=3

# Allow to perform insecure SSL requests to cinder (boolean
# value)
#cinder_api_insecure=false

# Allow attach between instance and volume in different
# availability zones. (boolean value)
#cinder_cross_az_attach=true


nova.section('hyperv')

#
# Options defined in nova.virt.hyperv.pathutils
#

# The name of a Windows share name mapped to the
# "instances_path" dir and used by the resize feature to copy
# files to the target host. If left blank, an administrative
# share will be used, looking for the same "instances_path"
# used locally (string value)
#instances_path_share=


#
# Options defined in nova.virt.hyperv.utilsfactory
#

# Force V1 WMI utility classes (boolean value)
#force_hyperv_utils_v1=false

# Force V1 volume utility class (boolean value)
#force_volumeutils_v1=false


#
# Options defined in nova.virt.hyperv.vif
#

# External virtual switch Name, if not provided, the first
# external virtual switch is used (string value)
#vswitch_name=<None>


#
# Options defined in nova.virt.hyperv.vmops
#

# Required for live migration among hosts with different CPU
# features (boolean value)
#limit_cpu_features=false

# Sets the admin password in the config drive image (boolean
# value)
#config_drive_inject_password=false

# qemu-img is used to convert between different image types
# (string value)
#qemu_img_cmd=qemu-img.exe

# Attaches the Config Drive image as a cdrom drive instead of
# a disk drive (boolean value)
#config_drive_cdrom=false

# Enables metrics collections for an instance by using
# Hyper-V's metric APIs. Collected data can by retrieved by
# other apps and services, e.g.: Ceilometer. Requires Hyper-V
# / Windows Server 2012 and above (boolean value)
#enable_instance_metrics_collection=false

# Enables dynamic memory allocation (ballooning) when set to a
# value greater than 1. The value expresses the ratio between
# the total RAM assigned to an instance and its startup RAM
# amount. For example a ratio of 2.0 for an instance with
# 1024MB of RAM implies 512MB of RAM allocated at startup
# (floating point value)
#dynamic_memory_ratio=1.0


#
# Options defined in nova.virt.hyperv.volumeops
#

# The number of times to retry to attach a volume (integer
# value)
#volume_attach_retry_count=10

# Interval between volume attachment attempts, in seconds
# (integer value)
#volume_attach_retry_interval=5


nova.section('zookeeper')

#
# Options defined in nova.servicegroup.drivers.zk
#

# The ZooKeeper addresses for servicegroup service in the
# format of host1:port,host2:port,host3:port (string value)
#address=<None>

# recv_timeout parameter for the zk session (integer value)
#recv_timeout=4000

# The prefix used in ZooKeeper to store ephemeral nodes
# (string value)
#sg_prefix=/servicegroups

# Number of seconds to wait until retrying to join the session
# (integer value)
#sg_retry_interval=5


nova.section('osapi_v3')

#
# Options defined in nova.api.openstack
#

# Whether the V3 API is enabled or not (boolean value)
#enabled=false

# A list of v3 API extensions to never load. Specify the
# extension aliases here. (list value)
#extensions_blacklist=

# If the list is not empty then a v3 API extension will only
# be loaded if it exists in this list. Specify the extension
# aliases here. (list value)
#extensions_whitelist=


nova.section('conductor')

#
# Options defined in nova.conductor.api
#

# Perform nova-conductor operations locally (boolean value)
#use_local=false
nova.param('use_local', type='boolean', default=False)

# the topic conductor nodes listen on (string value)
#topic=conductor
nova.param('topic', type='string', default='conductor')

# full class name for the Manager for conductor (string value)
#manager=nova.conductor.manager.ConductorManager

# Number of workers for OpenStack Conductor service (integer
# value)
#workers=<None>


nova.section('keymgr')

#
# Options defined in nova.keymgr
#

# The full class name of the key manager API class (string
# value)
#api_class=nova.keymgr.conf_key_mgr.ConfKeyManager


#
# Options defined in nova.keymgr.conf_key_mgr
#

# Fixed key returned by key manager, specified in hex (string
# value)
#fixed_key=<None>


nova.section('cells')

#
# Options defined in nova.cells.manager
#

# Cells communication driver to use (string value)
#driver=nova.cells.rpc_driver.CellsRPCDriver

# Number of seconds after an instance was updated or deleted
# to continue to update cells (integer value)
#instance_updated_at_threshold=3600

# Number of instances to update per periodic task run (integer
# value)
#instance_update_num_instances=1


#
# Options defined in nova.cells.messaging
#

# Maximum number of hops for cells routing. (integer value)
#max_hop_count=10

# Cells scheduler to use (string value)
#scheduler=nova.cells.scheduler.CellsScheduler


#
# Options defined in nova.cells.opts
#

# Enable cell functionality (boolean value)
#enable=false

# the topic cells nodes listen on (string value)
#topic=cells

# Manager for cells (string value)
#manager=nova.cells.manager.CellsManager

# name of this cell (string value)
#name=nova

# Key/Multi-value list with the capabilities of the cell (list
# value)
#capabilities=hypervisor=xenserver;kvm,os=linux;windows

# Seconds to wait for response from a call to a cell. (integer
# value)
#call_timeout=60

# Percentage of cell capacity to hold in reserve. Affects both
# memory and disk utilization (floating point value)
#reserve_percent=10.0

# Type of cell: api or compute (string value)
#cell_type=<None>

# Number of seconds after which a lack of capability and
# capacity updates signals the child cell is to be treated as
# a mute. (integer value)
#mute_child_interval=300

# Seconds between bandwidth updates for cells. (integer value)
#bandwidth_update_interval=600


#
# Options defined in nova.cells.rpc_driver
#

# Base queue name to use when communicating between cells.
# Various topics by message type will be appended to this.
# (string value)
#rpc_driver_queue_base=cells.intercell


#
# Options defined in nova.cells.scheduler
#

# Filter classes the cells scheduler should use.  An entry of
# "nova.cells.filters.all_filters"maps to all cells filters
# included with nova. (list value)
#scheduler_filter_classes=nova.cells.filters.all_filters

# Weigher classes the cells scheduler should use.  An entry of
# "nova.cells.weights.all_weighers"maps to all cell weighers
# included with nova. (list value)
#scheduler_weight_classes=nova.cells.weights.all_weighers

# How many retries when no cells are available. (integer
# value)
#scheduler_retries=10

# How often to retry in seconds when no cells are available.
# (integer value)
#scheduler_retry_delay=2


#
# Options defined in nova.cells.state
#

# Seconds between getting fresh cell info from db. (integer
# value)
#db_check_interval=60

# Configuration file from which to read cells configuration.
# If given, overrides reading cells from the database. (string
# value)
#cells_config=<None>


#
# Options defined in nova.cells.weights.mute_child
#

# Multiplier used to weigh mute children.  (The value should
# be negative.) (floating point value)
#mute_weight_multiplier=-10.0

# Weight value assigned to mute children.  (The value should
# be positive.) (floating point value)
#mute_weight_value=1000.0


#
# Options defined in nova.cells.weights.ram_by_instance_type
#

# Multiplier used for weighing ram.  Negative numbers mean to
# stack vs spread. (floating point value)
#ram_weight_multiplier=10.0


nova.section('database')

#
# Options defined in nova.openstack.common.db.api
#

# The backend to use for db (string value)
#backend=sqlalchemy

# Enable the experimental use of thread pooling for all DB API
# calls (boolean value)
#use_tpool=false


#
# Options defined in nova.openstack.common.db.sqlalchemy.session
#

# The SQLAlchemy connection string used to connect to the
# database (string value)
#connection=sqlite:////nova/openstack/common/db/$sqlite_db

# The SQLAlchemy connection string used to connect to the
# slave database (string value)
#slave_connection=

# timeout before idle sql connections are reaped (integer
# value)
#idle_timeout=3600

# Minimum number of SQL connections to keep open in a pool
# (integer value)
#min_pool_size=1

# Maximum number of SQL connections to keep open in a pool
# (integer value)
#max_pool_size=<None>

# maximum db connection retries during startup. (setting -1
# implies an infinite retry count) (integer value)
#max_retries=10

# interval between retries of opening a sql connection
# (integer value)
#retry_interval=10

# If set, use this value for max_overflow with sqlalchemy
# (integer value)
#max_overflow=<None>

# Verbosity of SQL debugging information. 0=None,
# 100=Everything (integer value)
#connection_debug=0

# Add python stack traces to SQL as comment strings (boolean
# value)
#connection_trace=false

# If set, use this value for pool_timeout with sqlalchemy
# (integer value)
#pool_timeout=<None>


nova.section('image_file_url')

#
# Options defined in nova.image.download.file
#

# A list of filesystems that will be configured in this file
# under the sections image_file_url:<list entry name> (list
# value)
#filesystems=


nova.section('baremetal')

#
# Options defined in nova.virt.baremetal.db.api
#

# The backend to use for bare-metal database (string value)
#db_backend=sqlalchemy


#
# Options defined in nova.virt.baremetal.db.sqlalchemy.session
#

# The SQLAlchemy connection string used to connect to the
# bare-metal database (string value)
#sql_connection=sqlite:///$state_path/baremetal_$sqlite_db


#
# Options defined in nova.virt.baremetal.driver
#

# Whether baremetal compute injects password or not (boolean
# value)
#inject_password=true

# Template file for injected network (string value)
#injected_network_template=$pybasedir/nova/virt/baremetal/interfaces.template

# Baremetal VIF driver. (string value)
#vif_driver=nova.virt.baremetal.vif_driver.BareMetalVIFDriver

# Baremetal volume driver. (string value)
#volume_driver=nova.virt.baremetal.volume_driver.LibvirtVolumeDriver

# a list of additional capabilities corresponding to
# instance_type_extra_specs for this compute host to
# advertise. Valid entries are name=value, pairs For example,
# "key1:val1, key2:val2" (list value)
#instance_type_extra_specs=

# Baremetal driver back-end (pxe or tilera) (string value)
#driver=nova.virt.baremetal.pxe.PXE

# Baremetal power management method (string value)
#power_manager=nova.virt.baremetal.ipmi.IPMI

# Baremetal compute node's tftp root path (string value)
#tftp_root=/tftpboot


#
# Options defined in nova.virt.baremetal.ipmi
#

# path to baremetal terminal program (string value)
#terminal=shellinaboxd

# path to baremetal terminal SSL cert(PEM) (string value)
#terminal_cert_dir=<None>

# path to directory stores pidfiles of baremetal_terminal
# (string value)
#terminal_pid_dir=$state_path/baremetal/console

# maximal number of retries for IPMI operations (integer
# value)
#ipmi_power_retry=5


#
# Options defined in nova.virt.baremetal.pxe
#

# Default kernel image ID used in deployment phase (string
# value)
#deploy_kernel=<None>

# Default ramdisk image ID used in deployment phase (string
# value)
#deploy_ramdisk=<None>

# Template file for injected network config (string value)
#net_config_template=$pybasedir/nova/virt/baremetal/net-dhcp.ubuntu.template

# additional append parameters for baremetal PXE boot (string
# value)
#pxe_append_params=<None>

# Template file for PXE configuration (string value)
#pxe_config_template=$pybasedir/nova/virt/baremetal/pxe_config.template

# Timeout for PXE deployments. Default: 0 (unlimited) (integer
# value)
#pxe_deploy_timeout=0

# If set, pass the network configuration details to the
# initramfs via cmdline. (boolean value)
#pxe_network_config=false

# This gets passed to Neutron as the bootfile dhcp parameter
# when the dhcp_options_enabled is set. (string value)
#pxe_bootfile_name=pxelinux.0


#
# Options defined in nova.virt.baremetal.tilera_pdu
#

# ip address of tilera pdu (string value)
#tile_pdu_ip=10.0.100.1

# management script for tilera pdu (string value)
#tile_pdu_mgr=/tftpboot/pdu_mgr

# power status of tilera PDU is OFF (integer value)
#tile_pdu_off=2

# power status of tilera PDU is ON (integer value)
#tile_pdu_on=1

# power status of tilera PDU (integer value)
#tile_pdu_status=9

# wait time in seconds until check the result after tilera
# power operations (integer value)
#tile_power_wait=9


#
# Options defined in nova.virt.baremetal.virtual_power_driver
#

# ip or name to virtual power host (string value)
#virtual_power_ssh_host=

# Port to use for ssh to virtual power host (integer value)
#virtual_power_ssh_port=22

# base command to use for virtual power(vbox,virsh) (string
# value)
#virtual_power_type=virsh

# user to execute virtual power commands as (string value)
#virtual_power_host_user=

# password for virtual power host_user (string value)
#virtual_power_host_pass=

# ssh key for virtual power host_user (string value)
#virtual_power_host_key=<None>


#
# Options defined in nova.virt.baremetal.volume_driver
#

# Do not set this out of dev/test environments. If a node does
# not have a fixed PXE IP address, volumes are exported with
# globally opened ACL (boolean value)
#use_unsafe_iscsi=false

# iSCSI IQN prefix used in baremetal volume connections.
# (string value)
#iscsi_iqn_prefix=iqn.2010-10.org.openstack.baremetal


nova.section('rpc_notifier2')

#
# Options defined in nova.openstack.common.notifier.rpc_notifier2
#

# AMQP topic(s) used for OpenStack notifications (list value)
#topics=notifications
nova.param('topics', type='stringlist', default='notifications')


nova.section('matchmaker_redis')

#
# Options defined in nova.openstack.common.rpc.matchmaker_redis
#

# Host to locate redis (string value)
#host=127.0.0.1

# Use this port to connect to redis host. (integer value)
#port=6379

# Password for Redis server. (optional) (string value)
#password=<None>


nova.section('ssl')

#
# Options defined in nova.openstack.common.sslutils
#

# CA certificate file to use to verify connecting clients
# (string value)
#ca_file=<None>

# Certificate file to use when starting the server securely
# (string value)
#cert_file=<None>

# Private key file to use when starting the server securely
# (string value)
#key_file=<None>


nova.section('trusted_computing')

#
# Options defined in nova.scheduler.filters.trusted_filter
#

# attestation server http (string value)
#attestation_server=<None>

# attestation server Cert file for Identity verification
# (string value)
#attestation_server_ca_file=<None>

# attestation server port (string value)
#attestation_port=8443

# attestation web API URL (string value)
#attestation_api_url=/OpenAttestationWebServices/V1.0

# attestation authorization blob - must change (string value)
#attestation_auth_blob=<None>

# Attestation status cache valid period length (integer value)
#attestation_auth_timeout=60


nova.section('upgrade_levels')

#
# Options defined in nova.baserpc
#

# Set a version cap for messages sent to the base api in any
# service (string value)
#baseapi=<None>


#
# Options defined in nova.cells.rpc_driver
#

# Set a version cap for messages sent between cells services
# (string value)
#intercell=<None>


#
# Options defined in nova.cells.rpcapi
#

# Set a version cap for messages sent to local cells services
# (string value)
#cells=<None>


#
# Options defined in nova.cert.rpcapi
#

# Set a version cap for messages sent to cert services (string
# value)
#cert=<None>


#
# Options defined in nova.compute.rpcapi
#

# Set a version cap for messages sent to compute services
# (string value)
#compute=<None>


#
# Options defined in nova.conductor.rpcapi
#

# Set a version cap for messages sent to conductor services
# (string value)
#conductor=<None>


#
# Options defined in nova.console.rpcapi
#

# Set a version cap for messages sent to console services
# (string value)
#console=<None>


#
# Options defined in nova.consoleauth.rpcapi
#

# Set a version cap for messages sent to consoleauth services
# (string value)
#consoleauth=<None>


#
# Options defined in nova.network.rpcapi
#

# Set a version cap for messages sent to network services
# (string value)
#network=<None>


#
# Options defined in nova.scheduler.rpcapi
#

# Set a version cap for messages sent to scheduler services
# (string value)
#scheduler=<None>


nova.section('matchmaker_ring')

#
# Options defined in nova.openstack.common.rpc.matchmaker_ring
#

# Matchmaker ring file (JSON) (string value)
#ringfile=/etc/oslo/matchmaker_ring.json


nova.section('vmware')

#
# Options defined in nova.virt.vmwareapi.driver
#

# URL for connection to VMware ESX/VC host. Required if
# compute_driver is vmwareapi.VMwareESXDriver or
# vmwareapi.VMwareVCDriver. (string value)
#host_ip=<None>

# Username for connection to VMware ESX/VC host. Used only if
# compute_driver is vmwareapi.VMwareESXDriver or
# vmwareapi.VMwareVCDriver. (string value)
#host_username=<None>

# Password for connection to VMware ESX/VC host. Used only if
# compute_driver is vmwareapi.VMwareESXDriver or
# vmwareapi.VMwareVCDriver. (string value)
#host_password=<None>

# Name of a VMware Cluster ComputeResource. Used only if
# compute_driver is vmwareapi.VMwareVCDriver. (multi valued)
#cluster_name=<None>

# Regex to match the name of a datastore. Used only if
# compute_driver is vmwareapi.VMwareVCDriver. (string value)
#datastore_regex=<None>

# The interval used for polling of remote tasks. Used only if
# compute_driver is vmwareapi.VMwareESXDriver or
# vmwareapi.VMwareVCDriver. (floating point value)
#task_poll_interval=5.0

# The number of times we retry on failures, e.g., socket
# error, etc. Used only if compute_driver is
# vmwareapi.VMwareESXDriver or vmwareapi.VMwareVCDriver.
# (integer value)
#api_retry_count=10

# VNC starting port (integer value)
#vnc_port=5900

# Total number of VNC ports (integer value)
#vnc_port_total=10000

# VNC password (string value)
#vnc_password=<None>

# Whether to use linked clone (boolean value)
#use_linked_clone=true


#
# Options defined in nova.virt.vmwareapi.vif
#

# Physical ethernet adapter name for vlan networking (string
# value)
#vlan_interface=vmnic0


#
# Options defined in nova.virt.vmwareapi.vim
#

# Optional VIM Service WSDL Location e.g
# http://<server>/vimService.wsdl. Optional over-ride to
# default location for bug work-arounds (string value)
#wsdl_location=<None>


#
# Options defined in nova.virt.vmwareapi.vim_util
#

# The maximum number of ObjectContent data objects that should
# be returned in a single result. A positive value will cause
# the operation to suspend the retrieval when the count of
# objects reaches the specified maximum. The server may still
# limit the count to something less than the configured value.
# Any remaining objects may be retrieved with additional
# requests. (integer value)
#maximum_objects=100


#
# Options defined in nova.virt.vmwareapi.vmops
#

# Name of Integration Bridge (string value)
#integration_bridge=br-int


nova.section('spice')

#
# Options defined in nova.spice
#

# location of spice html5 console proxy, in the form
# "http://127.0.0.1:6082/spice_auto.html" (string value)
#html5proxy_base_url=http://127.0.0.1:6082/spice_auto.html

# IP address on which instance spice server should listen
# (string value)
#server_listen=127.0.0.1

# the address to which proxy clients (like nova-
# spicehtml5proxy) should connect (string value)
#server_proxyclient_address=127.0.0.1

# enable spice related features (boolean value)
#enabled=false

# enable spice guest agent support (boolean value)
#agent_enabled=true

# keymap for spice (string value)
#keymap=en-us

nova.commit()

