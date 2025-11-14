/*
file: detail.tsx
description: Detail screen component for the React Native app
author: Anna Ni (annani@bu.ed)
*/
import { ScrollView, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function DetailScreen() {
  return (
    <ScrollView style={styles.scrollContainer}>
      <Text style={styles.titleText}>My Interests</Text>
      
      <Text style={styles.bodyText}>
        GRAPHIC DESIGN
      </Text>
      
      <Image
        source={{ uri: 'https://i.pinimg.com/736x/52/ba/7c/52ba7cd36df3b9cfce4d891ad9901e69.jpg' }}
        style={styles.detailImage}
        resizeMode="cover"
      />
      
      
      <Text style={styles.bodyText}>
        WEB DEVELOPMENT
      </Text>
      
      <Image
        source={{ uri: 'https://www.smartosc.com/wp-content/uploads/2023/12/web-app-development-min-e1703598852874.png' }}
        style={styles.detailImage}
        resizeMode="cover"
      />
      
      
      <Text style={styles.bodyText}>
        UI/UX DESIGN
      </Text>
      
      <Image
        source={{ uri: 'https://i.pinimg.com/736x/61/e7/9a/61e79a7b322d044d2fb3829567bafe57.jpg' }}
        style={styles.detailImage}
        resizeMode="cover"
      />
      
      <Text style={styles.bodyText}>
        Every project is an opportunity to learn and grow as a developer.
      </Text>
    </ScrollView>
  );
}