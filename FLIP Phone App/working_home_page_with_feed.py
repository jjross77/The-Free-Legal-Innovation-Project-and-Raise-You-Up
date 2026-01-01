

import { Platform, StyleSheet, View, Modal,Text,KeyboardAvoidingView,Button } from 'react-native';
import React from 'react';
import SearchInput from '../components/SearchInput';
import handleChangeText from '../components/SearchInput';
import Feed from './Feed';

export default class HomeScreen extends React.Component {
      state={text: 'd',
      cat:'kj',
      issues:[]
      }
       handleSubmitt = text => {

         this.setState({
           text:{text}  });
           return (
             <View style={styles.toolbar}>
               <SearchInput
                 placeholder="Type in your Legal Issue"
                 navigation={issue_navigation}
                 handleSubmitt={() => this.handleSubmitt()}
               /> 
               
             </View>
           );
           
      
       }

  render() {
      const {issue_navigation} = this.props;
      const {text}= this.state;
      const {issues}= this.state;

      

    return (

     <KeyboardAvoidingView style={styles.container} behavior="padding">

               <SearchInput
                 placeholder="Type in your Legal Issue"
                 navigation={issue_navigation}
                 handleSubmitt={() => this.handleSubmitt()}
               /> 
                <Feed style={styles.feed} /> 
                <Button
  title={text}
  onPress={issue_navigation}
/>
                                   

     </KeyboardAvoidingView>

    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  feed: {
    flex: 1,
    //marginTop:
    //  Platform.OS === 'android' || platformVersion < 11
    //    ? Constants.statusBarHeight
    //    : 0,
  },
});
