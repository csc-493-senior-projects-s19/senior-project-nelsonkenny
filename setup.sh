'''The purpose of this file is to setup the virtual environment
   In order to run the app you must use the command "source setup.sh"'''

# Establish variables for specific versions of libraries
FLASK_VERSION="${FLASK_VERSION:-0.11.1}"
PEEWEE_VERSION="${PEEWEE_VERSION:-2.8.1}"
FLASK_ADMIN_VERSION="${FLASK_ADMIN_VERSION:-1.4.0}"
WTF_PEEWEE_VERSION="${WTF_PEEWEE_VERSION:-0.2.6}"

# Check for virtualenv
command -v virtualenv >/dev/null 2>&1 || {
    echo >&2 "setup.sh requires 'virtualenv' but it is not installed";
    exit 1;
}

# Check for pip
command -v pip >/dev/null 2>&1 || { 
 echo >&2 "source.sh requires 'pip' but it's not installed."; 
 exit 1;
}

# Create the data directory if it doesn't exist
mkdir -p data

# Create a virtual machine virtual environment
if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

# upgrade pip 
pip install --upgrade pip

#install libraries needed for software

pip install -U "flask==$FLASK_VERSION"
# http://flask.pocoo.org/

pip install -U "peewee==$PEEWEE_VERSION"
# http://docs.peewee-orm.com/en/latest/

pip install -U "flask-admin==$FLASK_ADMIN_VERSION"
# https://flask-admin.readthedocs.io/en/latest/

pip install -U "wtf-peewee==$WTF_PEEWEE_VERSION"
# https://github.com/coleifer/wtf-peewee

pip install XlsxWriter

pip install pyyaml

pip install email_validator

pip install pyDNS