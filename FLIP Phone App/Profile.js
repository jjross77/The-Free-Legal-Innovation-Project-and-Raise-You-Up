import React from 'react';
import { StyleSheet, View } from 'react-native';

import ContactThumbnail from '../components/ContactThumbnail';
import DetailListItem from '../components/DetailListItem';

import colors from '../utils/colors';
import store from '../store';

export default class Profile extends React.Component {
constructor(props) {
    super(props);
    this.state = {
        person:{
           name:props.navigation.getParam('name'),
            phone:props.navigation.getParam('phone'),
            // name:'Raushan',
          //   phone:9931428888
        },
        textMessage: ''
    };
  
      const { id } = route.params;

    const { name } = store
      .getState()
      .contacts.find(contact => contact.id === id);

    return {
      title: name.split(' ')[0],
      headerTintColor: 'white',
      headerStyle: {
        backgroundColor: colors.blue,
      },
    };
  };

  state = store.getState();

  render() {
    const navigation = useNavigation();

    const { itemId, otherParam } = route.params;

    //const { navigation } = this.props;
    const { id } = this.props.route.params.id

  //const { id } = navigation.getParam(id, 'NO-ID')
  
    //    const { id } = route.params;

  //const{id}=navigation.state.params
  //const{id} = navigation.getParam('id')
  //const{id} =this.props.navigation.getParam(id)
    //const { navigation: { state: { params } } } = this.props;
    //const { id } = params;
    const {
      avatar, name, email, phone, cell,
    } = this.state.contacts.find(contact => contact.id === id);

    return (
      <View style={styles.container}>
        <View style={styles.avatarSection}>
          <ContactThumbnail avatar={avatar} name={name} phone={phone} />
        </View>
        <View style={styles.detailsSection}>
          <DetailListItem icon="mail" title="Email" subtitle={email} />
          <DetailListItem icon="phone" title="Work" subtitle={phone} />
          <DetailListItem icon="smartphone" title="Personal" subtitle={cell} />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  avatarSection: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: colors.blue,
  },
  detailsSection: {
    flex: 1,
    backgroundColor: 'white',
  },
});
