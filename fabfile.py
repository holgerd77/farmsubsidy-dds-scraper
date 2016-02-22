from fabric.api import env, roles, run, sudo

env.roledefs = {
    'scraper': ['ubuntu@openfarmsubsidies.org'],
}

env.key_filename = '~/.ssh/open-farmsubsidies.pem'
env.activate = 'source ~/venv-scraper/bin/activate'
env.code_dir = '/home/ubuntu/farmsubsidy-dds-scraper/'

@roles('scraper')
def prepare_system():
    sudo('apt-get update')
    sudo('apt-get upgrade')

@roles('scraper')
def install_deps():
    deps = [
        'git', 'nginx', 'supervisor',
        'python3', 'python3-pip', 'python3-dev', 'python-venv',
        'libxml2-dev', 'libffi-dev', 'libssl-dev', 'libxslt1-dev', 'libjpeg-dev',
    ]
    sudo('apt-get install ' + ' '.join(deps))
    
    