#!groovy

node {
        stage('Pulling from Github'){
            checkout scm
            stash includes: '*', name: 'pysource'
        }
}
// parallel unitTests: {
stage("UnitTesting") {
    echo "Running Unit tests"
    runTox("py27", "${env.PYTHON2}")
    runTox("py35", "${env.PYTHON3}")
}

node {
    try {
        stage("Generating Documentation"){
            unstash 'pysource'
            echo 'Creating virtualenv for generating docs'
            sh 'virtualenv -p $PYTHON2 venv_doc'
            sh '. ./venv_doc/bin/activate && \
            pip install Sphinx && \
            python setup.py build_sphinx'
            sh 'tar -czvf HtmlDocs.tar.gz -C build/sphinx/html .'
            archiveArtifacts artifacts: 'HtmlDocs.tar.gz'

        }

    } catch(error) {
        echo 'Unable to generate Sphinx documentation'
    }
}


def runTox(python_version, python_path)
{
    stage("Running Tox test in ${python_version}"){
      node {
        unstash 'pysource'
        withEnv(["PATH=${python_path}:${env.PATH}"]){
            sh "$TOX -e ${python_version}"
        }
        junit '**/junit-*.xml'
      }

    }
}
