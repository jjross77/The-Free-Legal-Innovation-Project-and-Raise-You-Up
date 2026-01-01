

import { Platform,
 ActivityIndicator,
 ImageBackground,
 KeyboardAvoidingView,
 StyleSheet,
 Text,
 StatusBar,
  View,
   Modal,
   Button } from 'react-native';
import React from 'react';
import SearchInput from '../components/SearchInput';
import handleChangeText from '../components/SearchInput';
import Feed from './Feed';

export default class HomeScreen extends React.Component {
state = {
  loading: true,
  error: false,
  location: '',
  temperature: 0,
  weather: '',
  text: 'd',
  cat:'kj',
  issue:'d',
  issue_sentences:'kj',
    casee:'kj',
    date:'kj'
};
      componentDidMount() {// here we want to display the feed results
        this.handleUpdateIssue('San Francisco');
      }
      

      handleUpdateIssue = async issue => {// this is imported into search input below and is then used in hand submitedtting as on submit prop
        if (!issue) return;
        
        //this is what we need to add intot he orignal update location
        console.log(`Pressed link! ${issue}`);

        this.setState({ loading: true }, async () => {
        
                this.setState({issue:issue});

        
          try {

            const { issue_sentences, casee, date,other_attributes } = await fetch_legal_issues(issue);
            this.setState({loading: false, error: false,issue_sentences,casee,date, });
          } catch (e) {
            this.setState({ loading: false, error: true });
          }
        });
      };

      render() {
              const { loading, error, issue_sentences,  casee,date,issue } = this.state;
              const {issue_navigation} = this.props;

        return (

          <KeyboardAvoidingView style={styles.container} behavior="padding">
            <StatusBar barStyle="light-content" />
            
             <Feed style={styles.feed} /> 
             <SearchInput
               placeholder="Type in your Legal Issue"
               onSubmit={this.handleUpdateIssue}
             />
            <ActivityIndicator animating={loading} color="white" size="large" />
            


              <View style={styles.container}>
              <Text style={[styles.largeText, styles.textStyle]}>
              {`Pressed link! ${issue}` }                      
              </Text>

                
              </View>
          </KeyboardAvoidingView>
        );
      }
    }
    


  


const styles = StyleSheet.create({
  container: {
    flex: 0,
    backgroundColor: 'white',
  },

  
  detailsContainer: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor:  'white',
    paddingHorizontal: 20,
  },
  textStyle: {
    textAlign: 'center',
    fontFamily: Platform.OS === 'ios' ? 'AvenirNext-Regular' : 'Roboto',
    color: 'black',
  },
  largeText: {
    fontSize: 44,
    color: 'black',
  },
  smallText: {
    fontSize: 18,
    color: 'black',
  },
});