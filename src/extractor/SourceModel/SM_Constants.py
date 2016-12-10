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
#ONLY_REQUIRE_REGEX = r'\s*require\s*(\=\>|\:)\s*'
ONLY_REQUIRE_REGEX    = r'\s*require\s*\=\>\s*'
ONLY_NOTIFY_REGEX     = r'\s*notify\s*\=\>\s*'
ONLY_ENSURE_REGEX     = r'\s*ensure\s*\=\>\s*'
ONLY_ALIAS_REGEX      = r'\s*alias\s*\=\>\s*'
ONLY_SUBSCRIBE_REGEX  = r'\s*subscribe\s*\=\>\s*'
ONLY_CONSUME_REGEX    = r'\s*consume\s*\=\>\s*'
ONLY_EXPORT_REGEX     = r'\s*export\s*\=\>\s*'
ONLY_SCHEDULE_REGEX   = r'\s*schedule\s*\=\>\s*'
ONLY_STAGE_REGEX      = r'\s*stage\s*\=\>\s*'
ONLY_TAG_REGEX        = r'\s*tag\s*\=\>\s*'
ONLY_NOOP_REGEX       = r'\s*noop\s*\=\>\s*'
ONLY_BEFORE_REGEX     = r'\s*before\s*\=\>\s*'
ONLY_AUDIT_REGEX      = r'\s*audit\s*\=\>\s*'
ONLY_SQL_REGEX        = r'\s*sql\s*\:\:\s*'
POSTGRES_REGEX        = r'\s*postgres\s*\:\:\s*'
### six elments to detect C syntax : typedef, char, int, void , unsigned, CMODSTART
ONLY_TYPEDEF_REGEX    = r'\w*\s*typedef\s*\w*\{\w*\}\;'
#ONLY_CHAR_REGEX      = r'\w*\s*char\s*\w*'
#ONLY_INT_REGEX       = r'\w*\s*int\s*\w*'
ONLY_VOID_REGEX       = r'\w*\s*void\s*\w*'
ONLY_UNSIGN_REGEX     = r'\w*\s*unsigned\s*\w*\;'
ONLY_CMODE_REGEX      = r'(?:^|\n)C_MODE_START'
ONLY_MCX_REGEX        = r'\s*mcx\s*\{'
ONLY_RSYSLOG_REGEX    = r'\s*rsyslog\:\:'
VALIDATE_HASH_REGEX   = r'(?:^|\n)validate\_hash\('
REQUIRE_PACK_REGEX    = r'(?:^|\n)require\_package\('
HIERA_INCL_REGEX      = r'(?:^|\n)hiera\_include\('
INCL_PACK_REGEX       = r'(?:^|\n)include\_packages\('
ENSU_PACK_REGEX       = r'(?:^|\n)ensure\_packages\('
CLASS_PARAM_REGEX     = r'class \w*[\:\:]*\w*\(.+\)\s*[\w*|\{]+'
ONLY_UNDEF_REGEX      = r'\s*undef\s*\=\>\s*'
ONLY_GIT_REGEX        = r'\w*\s*git\s*\w*'
INAVLID_GIT_REGEX     = r'\w*\s*.git\s*\w*'
#### Added Oct 15, 2016
VAR_ASSIGN_REGEX      = r'\$\w+\s*\=\s*\w+'
#### Added Oct 16, 2016
COLON_REQI_REGEX      = r'(?:^|\n)\s*(?:require) (?:Class)*\[*(?:\$|\')*[\w\d\:\-_\']+(?:\:\:\${0,1}[\w\d\:\-_\']+)*\'*\]*(?:\s*,\s*(?:Class)*\[*(?:\$|\')*[\w\d\:\-_\']+(?:\:\:\${0,1}[\w\d\:\-_\']+)*\'*\]*)*'
ONLY_ENV_REGEX        = r'\s*env\:\:\s*\w+'
ONLY_CRON_REGEX       = r'\s*cron\s*\{'
ONLY_REFF_REGEX       = r'\w+\s*\=\>\s*.+'  ### gives the count of '=>' s
##### Added Oct 17, 2016
INVALID_CLASS_REGEX   = r'\s*\#+.+class [\w\d\:\-_\']+(?:\:\:[\w\d\:\-_\']+)*\s*(?:\(.+\)\s*)*{*'
INVALID_DEFINE_REGEX  = r'\s*\#+.+define\s*\w*'
