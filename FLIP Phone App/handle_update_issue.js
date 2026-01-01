import { useState } from 'react';

//import fetch_legal_issues from './fetch_legal_issues';
function handleUpdateIssue  ({issue})  {// this is imported into search input below and is then used in hand submitedtting as on submit prop
  
  if (!issue) return;
  
  //this is what we need to add intot he orignal update location
  console.log(`Pressed link! ${issue}`);
    console.log(`Pressed link! ${issue}`);
    


   issueSetState({issue});
    //try {
    //  const { issue_sentences, casee, date,other_attributes } = await fetch_legal_issues(issue);
    //  this.setState({loading: false, error: false,issue_sentences,casee,date, });
   // } catch (e) {
   //   this.setState({ loading: false, error: true });
    //}
 // });
};

