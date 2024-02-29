node {
   def mvnHome
  stage('Prepare') {
      git url: 'https://github.com/cvadevops/b78am.git', branch: 'Jfrog'
      mvnHome = tool 'maven'
   }
  //stage ('Code Scanning') {
    //  sh "'${mvnHome}/bin/mvn' sonar:sonar"
  }

  stage ('Clean') {
      sh "'${mvnHome}/bin/mvn'  clean"
  }
  stage ('Validate') {
      sh "'${mvnHome}/bin/mvn'  validate"
  }
  stage ('Compile') {
      sh "'${mvnHome}/bin/mvn'  compile"
  }
  stage ('Test') {
      sh "'${mvnHome}/bin/mvn'  test"
  }
  stage ('Package') {
      sh "'${mvnHome}/bin/mvn'  package"
  }
  stage ('Verify') {
      sh "'${mvnHome}/bin/mvn'  verify"
  }
  stage ('Install') {
      sh "'${mvnHome}/bin/mvn'  install"
  }
  stage ('Deliver Artifact to Tomcat') {
      sh 'curl -u admin:redhat@123 -T target/**.war "http://34.201.218.148:8080/manager/text/deploy?path=/opswork&update=true"'
  }
  stage ('SmokeTest') {
      sh 'curl --retry-delay 10 --retry 5 "http://34.201.218.148:8080/opswork"'
  }

 }
