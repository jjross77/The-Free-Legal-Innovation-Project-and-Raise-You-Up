

// going to have to create the feedtype  state prop at one point 
//feed_type={feedd} this way
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

export default class IssuesScreen extends React.Component {
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
    start_fia_nn:true,
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
              const { loading, error, issue_sentences,  casee,date,issue,start_fia_nn,text } = this.state;
              const {issue_navigation} = this.props;

        return (
          <KeyboardAvoidingView style={styles.container} behavior="padding">
                    <Button title={text} onPress={issue_navigation}/>


            <StatusBar barStyle="light-content" />
             
            <ActivityIndicator animating={loading} color="white" size="large" />
            
            {!loading && (
            
              <View style={styles.container} behavior="padding">
              
                {error &&  (

                 <Text style={[styles.smallText, styles.textStyle]}>
                    {`This is the error for homescreen! ${issue}` } 
                  </Text>
                        )}
                        
            {!error && !start_fia_nn  
            ?  <View style={styles.container} behavior="padding">
            
             <SearchInput
               placeholder="Type in your Legal Issue"
               onSubmit={this.handleUpdateIssue}/>
               <Feed style={styles.textStyle,styles.smallText} />
             </View>
            : null } 
            
             {error && start_fia_nn  // will need to change the error here to ! so this does not display when error but only hwen not error just for display purposes now
             ?  <View style={styles.container} behavior="padding">
              <SearchInput
                placeholder="Type in your Legal Issue"
                onSubmit={this.handleUpdateLocation}/>
               <Feed  
               style={styles.textStyle,styles.smallText}  />
                 </View>
             : null }
             
              </View>
              
            )}
            
      </KeyboardAvoidingView>
    );
  }
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
  },
  feed: {
    flex: 1,
    fontSize: 18,
  },

  
  detailsContainer: {
    flex: 0,
    justifyContent: 'center',
    backgroundColor:  'black',
    paddingHorizontal: 20,
    color: 'black',
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
   
// use the contacts page as a template for this 
// and then have the contacts page reload for each category sub level
// use this same strategy for library as well          

