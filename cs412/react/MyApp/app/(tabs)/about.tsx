/*file: about.tsx
description: About screen component for the React Native app
author: Anna Ni (annani@bu.edu)
*/
import { View, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function AboutScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>About This App</Text>
      
      
      <Text style={styles.bodyText}>
        Hello World! This app is a simple demonstration of a mobile application using React Native. Below you will see a 2x2 image of the React
      </Text>
      
      <Image
        source={require('../../assets/images/favicon.png')}
        resizeMode="cover"
      />

      <Text style={styles.bodyText}>
        The app includes three main sections:
        {'\n\n'}
        • Home: Introduction and overview
        {'\n'}
        • Detail: In-depth exploration of interests
        {'\n'}
        • About: Information about the app itself
      </Text>
      
    </View>
  );
}