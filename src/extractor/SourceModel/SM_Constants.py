CLASS_REGEX = r'class [\w\d\:\-_\']+(?:\:\:[\w\d\:\-_\']+)*\s*(?:\(.+\)\s*)*{*'
CLASS_NAME_REGEX = r'class ([\w\d\:\-_\']+(?:\:\:[\w\d\:\-_\']+)*)\s*(?:\(.+\)\s*)*{*'
DEFINE_REGEX = r'define \w+(?:\:\:\w+)*\s*(?:\(.+\)\s*)*{*'
FILE_REGEX = r'file\W*\{\W*\'.+\'\W*:|file\W*\{\W*\".+\"\W*:|file\W*{\W*\$.+\W*:'
PACKAGE_REGEX = r'package\W*\{\W*\'.+\'\W*:|package\W*\{\W*\".+\"\W*:|package\W*{\W*\$.+\W*:'
SERVICE_REGEX = r'service\W*\{\W*\'.+\'\W*:|service\W*\{\W*\".+\"\W*:|service\W*{\W*\$.+\W*:'
DECLARE_INCLUDE_REGEX = r'(?:^|\n)\s*(?:include|require|contain) (?:Class)*\[*(?:\$|\')*[\w\d\:\-_\']+(?:\:\:\${0,1}[\w\d\:\-_\']+)*\'*\]*(?:\s*,\s*(?:Class)*\[*(?:\$|\')*[\w\d\:\-_\']+(?:\:\:\${0,1}[\w\d\:\-_\']+)*\'*\]*)*'
#DECLARE_INCLUDE_REGEX = r'(?:^|\n)\s*(?:include|require|contain) (?:Class)?\[?((?:\'|\$)?[\w\d\:\-_]+(?:\:\:[\w\d\:\-_]+)*\'?)\]?(?:\s*,\s*(?:Class)?\[?((?:\'|\$)?[\w\d\:\-_]+(?:\:\:[\w\d\:\-_]+)*\'?)\]?)*'
#DECLARE_RESOURCE_REGEX = r'(?:^|\n)\s*class \{\s*(?:\'|\"|\$)?[\w\:\-_]+(?:\:\:\$?[\w\:\-_]+)*(?:\'|\")?\s*\:'
DECLARE_RESOURCE_REGEX = r'(?:^|\n)\s*class \{\s*(?:\'|\")?\:{0,2}(\$?[\w\d\:\-_]+(?:\:\:\$?[\w\d\:\-_]+)*)(?:\'|\")?\s*\:'
EXEC_REGEX = r'exec\W*\{\W*\'.+\'\W*:|exec\W*\{\W*\".+\"\W*:|exec\W*{\W*\$.+\W*:'
LOC_REGEX = r'\n'
IF_REGEX = r'if\W+.+\W*\{'
CASE_REGEX = r'case\W+.+\W*\{'
USER_REGEX = r'user\W*\{\W*.+:'
COMMENT_REGEX = r'\A#|\n#'
HARDCODED_VALUE_REGEX = r'= \d+|=> \d+|= .*\'.+?\s*(?:\(.+\)\s*)*\'|=> .*\'.+?\s*(?:\(.+\)\s*)*\'|' \
                        r'= .*\".+?\s*(?:\(.+\)\s*)*\"|=> .*\".+\s*(?:\(.+\)\s*)*\"'
NODE_REGEX = r'node\W*\w+(?:\:\:\w+)*\W+\{'
GLOBAL_VAR_REGEX = r'\$.+\W*='

CLASS_GROUP_REGEX = r'class (\w+(?:\:\:\w+)*)\s*(?:\(.+\)\s*)*{*'
CLASS_INH_REGEX = r'inherits (\w+(?:\:\:\w+)*){*'
FILE_GROUP_REGEX = r'file\W*\{\W*\'(.+)\'\W*:|file\W*\{\W*\"(.+)\"\W*:|file\W*{\W*(\$.+)\W*:'
PACKAGE_GROUP_REGEX = r'package\W*\{\W*\'(.+)\'\W*:|package\W*\{\W*\"(.+)\"\W*:|package\W*{\W*(\$.+)\W*:'
SERVICE_GROUP_REGEX = r'service\W*\{\W*\'(.+)\'\W*:|service\W*\{\W*\"(.+)\"\W*:|service\W*{\W*(\$.+)\W*:'

DEPENDENT_PACKAGE = r'Package\W*\[\'.+\'\]'
DEPENDENT_SERVICE = r'Service\W*\[\'.+\'\]'
DEPENDENT_FILE = r'File\W*\[\'.+\'\]'
DEPENDENT_CLASS = r'Class\W*\[\'.+\'\]'

DEPENDENT_GROUP_PACKAGE = r'Package\W*\[\'(.+)\'\]'
DEPENDENT_GROUP_SERVICE = r'Service\W*\[\'(.+)\'\]'
DEPENDENT_GROUP_FILE = r'File\W*\[\'(.+)\'\]'
DEPENDENT_GROUP_CLASS = r'Class\W*\[\'(.+)\'\]'

PACKAGE = "Package"
FILE = "File"
SERVICE = "Service"
CLASS = "Class"

VAR1_REGEX = r'\$\{.+\}'
VAR2_REGEX = r'\$.+\W*\{'
VAR3_REGEX = r'\'.+\''
VAR4_REGEX = r'\".+\"'

VAR1_EX_REGEX = r'\$\{(.+)\}'
VAR2_EX_REGEX = r'\$(.+)\W*\{'
VAR3_EX_REGEX = r'\'(.+)\''
VAR4_EX_REGEX = r'\"(.+)\"'
#class\W+.+\{|

### Added Oct 14, 2016
ONLY_INCLUDE_REGEX    = r'(?:^|\n)\s*(?:include) (?:Class)*\[*(?:\$|\')*[\w\d\:\-_\']+(?:\:\:\${0,1}[\w\d\:\-_\']+)*\'*\]*(?:\s*,\s*(?:Class)*\[*(?:\$|\')*[\w\d\:\-_\']+(?:\:\:\${0,1}[\w\d\:\-_\']+)*\'*\]*)*'
ONLY_REQUIRE_REGEX    = r'\s*require\s*\=\>\s*'
ONLY_ENSURE_REGEX     = r'\s*ensure\s*\=\>\s*'
ONLY_BEFORE_REGEX     = r'\s*before\s*\=\>\s*'
CLASS_PARAM_REGEX     = r'class \w*[\:\:]*\w*\(.+\)\s*[\w*|\{]+'
VAR_ASSIGN_REGEX      = r'\$\w+\s*\=\s*\w+'
#### Added Oct 16, 2016
## Added Feb 17, 2017
ONLY_ENV_REGEX        = r'\s*env\:\:\s*\w+'
ONLY_CRON_REGEX       = r'\s*cron\s*\{'
ONLY_REFF_REGEX       = r'\w+\s*\=\>\s*.+'  ### gives the count of '=>' s
URL_REGEX             = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
UNLESS_REGEX          = r'\s*unless\s*\=\>\s*'
COND1_REGEX           = r'\w+\s*\>\=\s*.+'  ### gives the count of '>=' s
COND2_REGEX           = r'\w+\s*\<\=\s*.+'  ### gives the count of '<=' s
COND3_REGEX           = r'\w+\s*\=\=\s*.+'  ### gives the count of '==' s
NAMENODE_REGEX        = r'\s*namenode_hosts\s*\=\>\s*'
RUNINTERVAL_REGEX     = r'\s*runinterval\s*'
COMMAND_REGEX         = r'\s*command\s*\=\>\s*'
PATH_REGEX            = r'\s*path\s*\=\>\s*'
SSH_AUTH_REGEX        = r'ssh_authorized_key\W*\{\W*\'.+\'\W*:|ssh_authorized_key\W*\{\W*\".+\"\W*:|ssh_authorized_key\W*{\W*\$.+\W*:'
MODE_REGEX            = r'\s*mode\s*\=\>\s*'
ROLE_REGEX            = r'\s*role\s*\=\>\s*'
NAMESERVER_REGEX      = r'\s*nameserver\s*'
IPADDRESS_REGEX       = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
VIRTUAL_REGEX         = r'\s*realize\s*'
