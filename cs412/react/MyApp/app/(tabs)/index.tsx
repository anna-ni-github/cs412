/* file: index.tsx
description: Index screen component for the React Native app
author: Anna Ni (annani@bu.edu)
*/
import { View, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function IndexScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>Welcome to My App</Text>
      
      <Text style={styles.bodyText}>
        Hi this is the index page! You should see a picture of a monchichi below this text. 
      </Text>
      
      <Image
        source={require('../../assets/images/monchi.png')}
        style={styles.image}
        resizeMode="contain"
      />
      
      <Text style={styles.bodyText}>
        This app showcases my interests in technology and design. Feel free to 
        explore the different tabs to learn more!
      </Text>
    </View>
  );
}