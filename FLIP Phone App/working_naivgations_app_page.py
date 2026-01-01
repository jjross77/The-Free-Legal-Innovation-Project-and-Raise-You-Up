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
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import './gesture-handler';
import { fetchLocationId, fetchWeather } from './utils/api';
import SearchInput from './components/SearchInput';
import handleChangeText from './components/SearchInput';

//*screens/
//import Profile from './screens/Profile';
//import Options from './screens/Options';
import EntypoIcon from "react-native-vector-icons/Entypo"
import Ionicons from 'react-native-vector-icons/Ionicons'




function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
     <Button
        title="Go to library"
        onPress={() => {
          /* 1. Navigate to the Details route with params */
          navigation.navigate('library2', {
            itemId: 86,
            otherParam: 'anything you want here',
          });
        }}
      />
    </View>
  );
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

/* 2. Get the param */
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
    <Issues_Stack.Screen name="Friends" component={IssuesScreen} />
    <Issues_Stack.Screen
      name="library"
        component={LibraryScreen}
        options={({ route }) => ({ title: route.params.name })}
       />
  </Issues_Stack.Navigator>
);
}

function Library_screens() {
const Library_Stack = createStackNavigator();
return (
  <Library_Stack.Navigator>
    <Library_Stack.Screen name="Library" component={LibraryScreen} />
        <Issues_Stack.Screen name="library" component={LibraryScreen} />

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
    <Ionicons name="home" color={color} size={size} />
  ),
}} />
      <Tab.Screen name="Friends" component={Issues_screens}
      options={{
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








