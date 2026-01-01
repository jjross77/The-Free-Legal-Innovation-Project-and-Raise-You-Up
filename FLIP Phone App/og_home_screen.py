# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:34:29 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""



// use this for stack navigator
//import LibraryScreen from './screens/LibraryScreen';


export default class App extends React.Component {
  state = {
    loading: false,
    error: false,
    location: '',
    temperature: 0,
    weather: '',
  };

  Home_Display = ({ navigation }) => {// call it as a class in the return statement  to upload this as a seperate page
    return (
    <HomeScreen
    issue_navigation={() => navigation.navigate('Issues')}
    />
    );
  }
  Profile_display= ({ navigation }) => {//database search will go down tree of categories
    return (

     <Profile 
     navigation={navigation}
     />
     );
      }
      
   Issues_Display = ({ navigation }) => {//database search will go down tree of categories
     return (

      <IssuesScreen 
      issue_navigation={() => navigation.navigate('Home')}
      navigation={navigation}
      />
      );
       }
  Library_Display = ({ navigation }) => {// we will use messager app 
    return (
    ///USE THE COMMENTED OUT lines below ONCE SCREEN IS BUILT
    //<LibraryScreen
    //messages={messages}
    //onPressMessage={this.handlePressMessage}
    // />
              <View style={{  justifyContent: 'center', alignItems: 'center'}}>
                 <Ionicons
                   testID="nextButton"
                   name="cafe"
                   color="rgba(255, 255, 255, .9)"
                   size={24}
                   style={{backgroundColor: 'red'}}
                 />
                              <EntypoIcon size={30} color="red" icon="video-camera" />


        <Text>Home!</Text>


      </View>
    );
  }
  Home_screens_stack = () => {
      const Home_Stack = createStackNavigator();

    return (
      <Home_Stack.Navigator>
        <Home_Stack.Screen name="he" component={this.Home_Display} />
       
      </Home_Stack.Navigator>
    );
  } 
  Issues_screens_stack = () => {
        const Issues_Stack = createStackNavigator();

    return (
      <Issues_Stack.Navigator>
        <Issues_Stack.Screen name="Friends" component={this.Issues_Display} />
        <Issues_Stack.Screen name="Profile" component={this.Profile_display} />

       
      </Issues_Stack.Navigator>
    );
    }
    Library_screens_stack = () => {
          const Library_Stack = createStackNavigator();

      return (
        <Library_Stack.Navigator>
          <Library_Stack.Screen name="Home" component={this.Library_Display} />
        </Library_Stack.Navigator>
      );
      }
 

    render() {
      const Home_Stack = createStackNavigator();
      const Issues_Stack = createStackNavigator();
      const Library_Stack = createStackNavigator();
      const Tab = createBottomTabNavigator();
      const { number, error, location, weather, temperature } = this.state;
      return (
      <NavigationContainer>
        <Tab.Navigator>
        
          <Tab.Screen name="Home" component={this.Home_screens_stack}
          options={{
      tabBarLabel: 'Home',
      tabBarIcon: ({ color, size }) => (
        <Ionicons name="home" color={color} size={size} />
      ),
    }} />
          <Tab.Screen name="Friends" component={this.Issues_screens_stack}
          options={{
      tabBarLabel: 'Friends',
      tabBarIcon: ({ color, size }) => (
        <Ionicons name="cafe" color={color} size={size} />
      ),
      
    }}
           />
          <Tab.Screen name="Library" component={this.Library_screens_stack}
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
  }
  
  

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  imageContainer: {
    flex: 1,
  },
  container2: {
      fontSize: 10,
      backgroundColor: 'rgba(0,0,0,0.2)',
    flex: 1,
    backgroundColor: '#kkk',
  },
  
  
});
