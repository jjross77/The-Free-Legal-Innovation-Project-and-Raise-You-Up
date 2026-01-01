
import * as React from 'react';
import {
  ActivityIndicator,
  ImageBackground,
  KeyboardAvoidingView,
  Platform,
  StyleSheet,
  Text,
  TextInput,
  View,
  Button,
  StatusBar,
  FlatList
} from 'react-native';

//import fetch_legal_issues from './fetch_legal_issues';
 export default function process_legal_issue_input(issue,issueSetState2,issueSetState) { 
 const{nativeEvent: {text, eventCount, target}}=issue
  if (!issue) return;

  console.log(`Pressed link! ${text}`);
  issueSetState('')// this clears the search bar for us
  
  issueSetState2(text)// this is what we will use to rerender stuff and this way we can effect the return statement usin this
  // and build it into the page so when this changes it takes the results and rerenders some elements with a if statement depending on these values
  
  
  
  

    
}

 