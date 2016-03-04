from fabric.api import env, roles, run, sudo

env.roledefs = {
    'all': ['ubuntu@openfarmsubsidies.org'],
}

env.key_filename = '~/.ssh/open-farmsubsidies.pem'

@roles('all')
def prepare_system():
    sudo('apt-get update')
    sudo('apt-get upgrade')

@roles('all')
def install_deps():
    deps = [
        #Generic
        'git', 'nginx', 'supervisor', 'unzip', 'apache2-utils',
        #farmsubsidy-dds-scraper
        'python3', 'python3-pip', 'python3-dev', 'python-venv',
        'libxml2-dev', 'libffi-dev', 'libssl-dev', 'libxslt1-dev', 'libjpeg-dev',
        #farmsubsidy-dds-elastic
        'openjdk-7-jre',
        #farmsubsidy-dds-frontend
        'nodejs', 'npm',
    ]
    sudo('apt-get install ' + ' '.join(deps))
    
    