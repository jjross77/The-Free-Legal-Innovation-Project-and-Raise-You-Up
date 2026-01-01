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
import handleChangeText from './components/SearchInput';
import handleUpdateIssue from './Functions/handle_update_issue';
import Feed from './screens/Feed';
import renderContact from './Functions/render_contacts';
import store from './store';
import { fetchContacts } from './utils/api';

import { useEffect } from 'react';
import { useState } from 'react';


import EntypoIcon from "react-native-vector-icons/Entypo"
import Ionicons from 'react-native-vector-icons/Ionicons'


function HomeScreen({ navigation }) {
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
      onPress={() => navigation.navigate('library')}
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

function IssuesScreen({ navigation }) {

return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Issues Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('library')}
      />
    </View>
  );
}

function LibraryScreen({ navigation }) {

return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Library Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('library')}
      />
    </View>
  );
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








function Home_screens() {
const Home_Stack = createStackNavigator();

  return (
  <Home_Stack.Navigator>
    <Home_Stack.Screen name="start" component={HomeScreen} />
    <Home_Stack.Screen name="library" component={LibraryScreen} /> 
        <Home_Stack.Screen name="library2" component={LibraryScreen2} />  
                <Home_Stack.Screen name="library3" component={LibraryScreen3} />  
  </Home_Stack.Navigator>

  );
}

function Issues_screens() {
  const Issues_Stack = createStackNavigator();
return (
  <Issues_Stack.Navigator>
    <Issues_Stack.Screen name="Friends" component={IssuesScreen}
    options={{
      title: 'Issues',
      headerStyle: {
        backgroundColor: '#00008B',
      },
      headerTintColor: '#fff',
      headerTitleStyle: {
        fontWeight: 'bold',
      },
    }}
  />
    
   
       <Issues_Stack.Screen
        name="library"
        component={LibraryScreen}
        options={{
          title: 'library',
          headerStyle: {
            backgroundColor: '#f4511e',
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      />
  </Issues_Stack.Navigator>
);
}

function Library_screens() {
const Library_Stack = createStackNavigator();
return (
  <Library_Stack.Navigator>
    <Library_Stack.Screen name="Library" component={LibraryScreen} />
        <Library_Stack.Screen name="library" component={LibraryScreen} />

  </Library_Stack.Navigator>
);
}


export default function App() {
const Tab = createBottomTabNavigator();
  return (
  <NavigationContainer>
    <Tab.Navigator>
      <Tab.Screen name="Home" component={Home_screens}
      options={{
  tabBarLabel: 'Home',
  tabBarIcon: ({ color, size }) => (
    <Ionicons name="home" color={color} size={size} 
    
    
    
    
    />
  ),
}} />
      <Tab.Screen name="Issues" component={Issues_screens}
      options={{
                  headerStyle: {
            backgroundColor: '#00008B',
          },
          
  tabBarLabel: 'Friends',
  tabBarIcon: ({ color, size }) => (
    <Ionicons name="cafe" color={color} size={size} />
  ),
  
}}
       />
      <Tab.Screen name="Library" component={Library_screens}
      options={{
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
});







