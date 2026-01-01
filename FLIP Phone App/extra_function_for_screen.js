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



