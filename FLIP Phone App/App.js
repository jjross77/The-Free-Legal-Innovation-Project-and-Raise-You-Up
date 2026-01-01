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
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import './gesture-handler';
import { fetchLocationId, fetchWeather } from './utils/api';
import SearchInput from './components/SearchInput';
import Feed from './screens/Feed';



import renderContact from './Functions/render_contacts';
import handleUpdateIssue from './Functions/handle_update_issue';//use this for uploading results when ready for api from fia nn
import process_legal_issue_input from  './Functions/process_legal_issue_input';



import store from './store';
import { fetchContacts } from './utils/api';
import DetailListItem from './components/DetailListItem';


import { useEffect } from 'react';
import { useState } from 'react';


import EntypoIcon from "react-native-vector-icons/Entypo"
import Ionicons from 'react-native-vector-icons/Ionicons'
import MaterialIcons from 'react-native-vector-icons/MaterialIcons'





function HomeScreen({ navigation }) {
const [loading, loadingSetState] = useState(store.getState().isFetchingContacts)
const [error, errorSetState] = useState(store.getState().error)
const [issue, issueSetState] = useState('hi')
const [issue2, issueSetState2] = useState('')
const [issue3, issueSetState3] = useState('h')



const contactsSorted = fetchContacts();

const keyExtractor = ({ phone }) => phone;
const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'First Item',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Second Item',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Third Item',
  },
];
const Item = ({title}) => (// this is what we use to  modify what he flatlist looks like
  <View style={styles.textStyle}>
    <Text style={styles.textStyle}>{title}</Text>
    <Button
      title="Go to Details"
      onPress={() => issueSetState3('meow')}
    />
    
  </View>
);

useEffect(() => {// this is what we will use ot check if everything mounted
loadingSetState(false)// if loading is true or error is
// true it will not load this is what we want this sets loading to false so it will load

}, []);

  //const [text, onChangeText] = React.useState('Useless Text');



         return (
        <KeyboardAvoidingView style={styles.container} behavior="padding">
        {issue3==='meow'&&  <ActivityIndicator size="large" />}
        
        {issue3 != 'meow' &&  <Text style={[styles.smallText, styles.textStyle]}>
        {'This applies conditional rendering when the button is pressed showing a activity indicator use this for conditonal rendering of the page to display  results depending on what is pressed' }   
        </Text> }
        
          
        

         {loading && <ActivityIndicator size="large" />}
         {error && <Text>Error...</Text>}
         {!loading &&
           !error && (
            <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            
       <TextInput
        onChangeText={new_issue => issueSetState(new_issue)}
        placeholder='Type in your legal issue'
        placeholderTextColor="white"
        underlineColorAndroid="transparent"
        style={styles.textInput}
        clearButtonMode="always"
        value={issue}
        onSubmitEditing={new_issuee => process_legal_issue_input(new_issuee,issueSetState2,issueSetState)}
      />
      

             
                <Text style={[styles.smallText, styles.textStyle]}>
                   {`This is the issue variable  ${issue}` } 
                 </Text>
                 <Text style={[styles.smallText, styles.textStyle]}>
                    {`This is the issue2 variable ${issue2}` } 
                  </Text>
                  <Text style={[styles.smallText, styles.textStyle]}>
                     {`This is the issue3 variable ${issue3}` } 
                   </Text>
                   
                   
                   {issue3 != 'meow' &&  <Text style={[styles.smallText, styles.textStyle]}>
                   {'This applies conditional rendering when the button is pressed showing a activity indicator use this for conditonal rendering of the page to display  results depending on what is pressed' }   
                   </Text> }
                   
                   
                   
                 {issue2 && <FlatList
          data={DATA}
          renderItem={({item}) => <Item title={item.title} />}
          keyExtractor={item => item.id}/> }
                 
              
                </View>
                    )}               
                       </KeyboardAvoidingView>
                    
               

             )
}

function IssuesScreen({ navigation }) {
const [loading, loadingSetState] = useState(store.getState().isFetchingContacts)
const [error, errorSetState] = useState(store.getState().error)
const contactsSorted = fetchContacts();
const keyExtractor = ({ phone }) => phone;
const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'First Item',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Second Item',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Third Item',
  },
];
const Item = ({title}) => (// this is what we use to  modify what he flatlist looks like
  <View style={styles.textStyle}>
    <Text style={styles.textStyle}>{title}</Text>
    <Button
      title="Go to Details"
      onPress={() => navigation.navigate('Issues')}
    />
    
  </View>
);

useEffect(() => {// this is what we will use ot check if everything mounted
loadingSetState(false)// if loading is true or error is
// true it will not load this is what we want this sets loading to false so it will load

}, []);
         return (
        <KeyboardAvoidingView style={styles.container} behavior="padding">

         {loading && <ActivityIndicator size="large" />}
         {error && <Text>Error...</Text>}
         {!loading &&
           !error && (
            <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>

              <SearchInput
                placeholder="Type in your Legal Issue"
                onSubmit={handleUpdateIssue}/>
                
               <FlatList
        data={DATA}
        renderItem={({item}) => <Item title={item.title} />}
        keyExtractor={item => item.id}
      />
                </View>
                    )}
                       </KeyboardAvoidingView>
                    
               

             )
}
function LibraryScreen({ navigation }) {
const [loading, loadingSetState] = useState(store.getState().isFetchingContacts)
const [error, errorSetState] = useState(store.getState().error)
const contactsSorted = fetchContacts();// this is where we will get our data from the api
const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'Update Profile',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Change Language',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Sign Out',
  },
];
const Item = ({title}) => (// this is what we use to  modify what he flatlist looks like
  <View style={styles.textStyle}>
    <Button
      title={title}
      onPress={handleUpdateIssue}
    />
    
  </View>
);

useEffect(() => {// this is what we will use ot check if everything mounted
loadingSetState(false)// if loading is true or error is
// true it will not load this is what we want this sets loading to false so it will load

}, []);
         return (
        <KeyboardAvoidingView style={styles.container} behavior="padding">

         {loading && <ActivityIndicator size="large" />}
         {error && <Text>Error...</Text>}
         {!loading &&
           !error && (
            <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
 
               <FlatList
        data={DATA}
        renderItem={({item}) => <Item title={item.title} />}
        keyExtractor={item => item.id}
      />
                </View>
                    )}
                       </KeyboardAvoidingView>
                    
               

             )
}







function LibraryScreen2( { route, navigation }) {

  const { itemId, otherParam } = route.params;
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      <Text>itemId: {JSON.stringify(itemId)}</Text>
      <Text>otherParam: {JSON.stringify(otherParam)}</Text>
      <Button
        title="Go to Library... again"
        onPress={() =>
          navigation.push('library', {
            itemId: Math.floor(Math.random() * 100),
          })
        }
      />
      <Button title="Go to Home" onPress={() => navigation.navigate('start')} 

      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      
      <Button
        title="Go to library3"
        onPress={() => {
          // Pass and merge params back to home screen
          navigation.navigate({
            name: 'library3',
            params:  { user: 'jane' },
          });
        }}
      />

 </View>
  );
}

function LibraryScreen3( { route, navigation }) {

/* 2. Get the param */
  const { user } = route.params;
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      <Text>user: {JSON.stringify(user)}</Text>
      <Button
        title="Go to Library... again"
        onPress={() =>
          navigation.push('library', {
            itemId: Math.floor(Math.random() * 100),
          })
        }
      />
      <Button title="Go to Home" onPress={() => navigation.navigate('start')} 

      />
      <Button title="Go back" onPress={() => navigation.goBack()} />
    </View>
  );
}





export default function App() {
const Tab = createBottomTabNavigator();
  return (
  <NavigationContainer>
  
    <Tab.Navigator>
      <Tab.Screen name="Home" component={HomeScreen}
      options={{
      headerStyle: {
            backgroundColor: '#00008B',  },
headerTintColor: '#fff', 
      
  tabBarLabel: 'Home',
  tabBarIcon: ({ color, size }) => (
    <Ionicons name="home" color={color} size={size} 
 
    />
  ),
}} />
      <Tab.Screen name="Issues" component={IssuesScreen}
      options={{
                  headerStyle: {
            backgroundColor: '#00008B',},
headerTintColor: '#fff', 
  tabBarLabel: 'Issues',
  tabBarIcon: ({ color, size }) => (
    <MaterialIcons name="balance" color={color} size={size} />
  ),
  
}}
       />
      <Tab.Screen name="Library" component={LibraryScreen}
      options={{
      headerStyle: {
            backgroundColor: '#00008B',},
headerTintColor: '#fff',
  tabBarLabel: 'Library',
  tabBarIcon: ({ color, size }) => (
    <Ionicons name="book" color={color} size={size} />
  ),
}} />
    </Tab.Navigator>
  </NavigationContainer>
  );   
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
  search_input_container: {
    height: 50,
    marginTop: 20,
    backgroundColor: '#00008B',
    marginHorizontal: 40,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
  textInput: {
    color: 'white',
    height: 50,
    marginTop: 20,
    backgroundColor: '#00008B',
    marginHorizontal: 40,
    paddingHorizontal: 10,
    borderRadius: 5,
    
  },
});







