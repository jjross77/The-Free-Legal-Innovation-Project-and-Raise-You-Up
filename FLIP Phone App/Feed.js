import {
  ActivityIndicator,
  Text,
  ViewPropTypes,
   StyleSheet,
  SafeAreaView,
} from 'react-native';
import React from 'react';

import { fetchPosts } from '../utils/api_posts';// just need to write and create a fetch posts api to make this work now
//make fixes to the underlying scripts in feed like card and cardlist when you need to
//once you have the api written
import CardList from '../components/CardList';

export default class Feed extends React.Component {
  

  static defaultProps = {
    style: null,
  };

  state = {
    loading: true,
    error: false,
    items: [],
  };

  async componentDidMount() {
    try {
      const items = await fetchPosts();

      this.setState({
        loading: false,
        items,
      });
    } catch (e) {
      this.setState({
        loading: false,
        error: true,
      });
    }
  }

  render() {
    const { style } = this.props;
    const { loading, error, items } = this.state;

    if (loading) {
      return <ActivityIndicator size="large" />;
    }

    if (error) {
      return <Text style={style}> this is the Error for FEED...</Text>;
    }

    return (
      <SafeAreaView style={style}>
      <Text> hi</Text>
        <CardList items={items} />
      </SafeAreaView>
    );
  }
}
