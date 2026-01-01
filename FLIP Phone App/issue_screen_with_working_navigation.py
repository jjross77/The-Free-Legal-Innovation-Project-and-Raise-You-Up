 <KeyboardAvoidingView style={styles.container} behavior="padding">
         <Text>Settings!</Text>          
           <SearchInput
             placeholder="Type in your Legal Issue"
           />
            <Feed style={styles.feed} /> 
              <Button title={text} onPress={issue_navigation}/>
   </KeyboardAvoidingView>
   
         <KeyboardAvoidingView style={styles.container} behavior="padding">
                 <Text>Settings!</Text>          
                   <SearchInput
                     placeholder="Type in your Legal Issue"
                   />
                    <Button
      title="Go to Settings"
      onPress={() => navigation.navigate('Home')}
    />
         </KeyboardAvoidingView>