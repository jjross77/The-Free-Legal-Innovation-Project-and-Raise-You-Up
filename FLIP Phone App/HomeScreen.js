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
    start_fia_nn:true,
    feedd:false,
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
              const { loading, error, issue_sentences,  casee,date,issue,start_fia_nn,feedd } = this.state;
              const {issue_navigation} = this.props;

        return (

          <KeyboardAvoidingView style={styles.container} behavior="padding">
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
            
             <View style={styles.container}>
               {loading && <ActivityIndicator size="large" />}
               {error && <Text>Error...</Text>}
               {!loading &&
                 !error && (
                           <SearchInput
                             placeholder="Type in your Legal Issue"
                             onSubmit={this.handleUpdateIssue}/>

                   <FlatList
                     data={contactsSorted}
                     keyExtractor={keyExtractor}
                     renderItem={this.renderContact}
                   />
                 )}
             </View>
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