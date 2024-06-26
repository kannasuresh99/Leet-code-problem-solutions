// PR 171 Changes are Overridden because it is not planned and causing issues
@Library('pipelineLibrary') _

import com.statestreet.util.GetPasswordFromPwMatrix
import com.statestreet.util.CredentialsStore

pipeline{

    agent {label 'PRODLinux'}

    parameters {
    booleanParam(
            name: 'XDRYRUN',
            defaultValue: false,
            description: 'if true then a dry run, used to update the parameter definitions.  Will not run the job'
         )
        string(
            name: 'buildRequesterUserId',
            description: 'Build User ID'
         )
        string(
            description: 'ProjectName',
            name: 'projectname'
        )
        string(
            description: 'version',
            name: 'version'
        )
        choice(
            choices: ['PLANNING','DEVELOPMENT','RELEASED','DEPRECATED','ARCHIVED','PRERELEASE'],
            description: 'Required Phase',
            name: 'requiredphase'
        )

    }

    environment {
        bdtokendev = "${BlackduckToken_DEV}"
        bdtoken = "${BlackduckToken}"
        ci_env = "${CI_Env}"
    }

    stages {
       stage("Update Phase"){
            when {
                expression {
                    return env.XDRYRUN != null && env.XDRYRUN == "false" && env.buildRequesterUserId && env.ProjectName && env.version
                }
            }
            steps{
                script{
            print "execution started"
            print "${env.ci_env}"
            print "ci_env printed"
            def giturl
                    if ( ci_env == "PROD" ){
                                giturl = "https://gitprod.statestr.com/api/v3/orgs/"
                          }
                    else if ( ci_env == "UAT" ){
                                giturl = "https://gitua.statestr.com/api/v3/orgs/"
                          }
                    else {
                                giturl = "https://gitdev.it.statestr.com/api/v3/orgs/"
                          }

                    def appcode = projectname.substring(0,3)
            def gittemp = giturl + appcode.toUpperCase() + "/teams/ssc_" + appcode + "_devmgr/members | grep -c " + buildRequesterUserId
            println "gittempvar : $gittemp"

            def pwMatrixObj = new com.statestreet.util.GetPasswordFromPwMatrix(steps)
            pwMatrixObj.withCloakware([
                        credentialsId: "gitCloakwareCredential",
                        passwordVariable: 'gitpassword',
                        usernameVariable: 'gitusername',
                        comment: "github ${ci_env}"]){
                    def devmgrResponse = steps.sh(returnStdout: true, script: '''
                    set +xe
                    a=`curl -X GET --silent -u "${gitusername}":"${gitpassword}" -H 'Accept: application/vnd.github+json' '''+ gittemp +'''`
                    ''') 
            
            def apiBDUrl
            def apiBDToken
            if ( ci_env == "PROD" ){
                apiBDUrl = "https://statestreet.app.blackduck.com/"
            }else{
                apiBDUrl = "https://statestreet-sandbox.app.blackduck.com/"
            }

            pwMatrixObj.withCloakware([
                credentialsId: "BlackduckToken_Cloakware_Credential",
                passwordVariable: 'apiBDToken',
                usernameVariable: 'apiBDUsername',
                comment: "BlackDuck Token for ${ci_env}"
            ]) {
                sh'''
                set +xe
                cd ${WORKSPACE}/BDPhaseUpdate
                python BDphasechange.py '''+apiBDToken + " "+ apiBDUrl+''' "${projectname}" "${version}" "${requiredphase}"
                if [ $? -eq 0 ]
                then
                    echo "Phase Changing operation performed successfully"
                else
                    echo "Failed to update the phase for the project '${projectname}' and version '${version}'. Please see more details above."
                    exit 1
                fi
                '''

                  }
                        }
              }

         }
      }
  }
}