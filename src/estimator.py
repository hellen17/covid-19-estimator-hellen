def estimator(data):
  impact.currentlyInfected = data.reportedCases*10
  severeImpact.currentlyInfected = data.reportedCases*50

  InfectionsByRequestedTime = currentlyInfected * 512

  
  return{
    data,
    impact:{
      currentlyInfected:currentlyInfected
    }

  } 
