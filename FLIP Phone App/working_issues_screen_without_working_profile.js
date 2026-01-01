import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  ActivityIndicator,
  Linking,
} from 'react-native';

import ContactListItem from '../components/ContactListItem';

import { fetchContacts } from '../utils/api';
import getURLParams from '../utils/getURLParams';
import store from '../store';

const keyExtractor = ({ phone }) => phone;

export default class IssuesScreen extends React.Component { 
  state = {
    contacts: store.getState().contacts,
    loading: store.getState().isFetchingContacts,
    error: store.getState().error,
  };

  async componentDidMount() {
    this.unsubscribe = store.onChange(() =>
      this.setState({
        contacts: store.getState().contacts,
        loading: store.getState().isFetchingContacts,
        error: store.getState().error,
      }));

    const contacts = await fetchContacts();
    store.setState({ contacts, isFetchingContacts: false });
    //const subscription = Linking.addEventListener('url', onReceiveURL);

    //Linking.addEventListener('url', this.handleOpenUrl);
    //const linkingSubscription = Linking.addEventListener('url', ({ url }) => {
     // listener(url);

    //const url = await Linking.getInitialURL();
    //this.handleOpenUrl({ url });
  }

  componentWillUnmount() {
     // this.changeEventListener.remove()
    //Linking.removeEventListener('url', this.handleOpenUrl); //this is depreciated


    this.unsubscribe();
  }

  

  renderContact = ({ item }) => {
    const { navigation: { navigate } } = this.props;
    const {
      id, name, avatar, phone,
    } = item;

    return (
      <ContactListItem
        name={name}
        avatar={avatar}
        phone={phone}
        onPress={() =>
         navigate('Profile', { id })}
      />
    );
  };

  render() {
    const { contacts, loading, error } = this.state;

    const contactsSorted = contacts.sort((a, b) =>
      a.name.localeCompare(b.name));

    return (
      <View style={styles.container}>
        {loading && <ActivityIndicator size="large" />}
        {error && <Text>Error...</Text>}
        {!loading &&
          !error && (
            <FlatList
              data={contactsSorted}
              keyExtractor={keyExtractor}
              renderItem={this.renderContact}
            />
          )}
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'white',
    justifyContent: 'center',
    flex: 1,
  },
});
