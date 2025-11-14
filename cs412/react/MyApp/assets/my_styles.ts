/* Styles for a React Native application with a dark theme
*/
import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#000',  // Changed to black
  },
  scrollContainer: {
    flex: 1,
    padding: 20,
    backgroundColor: '#000',  // Changed to black
  },
  titleText: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 16,
    color: '#fff',  // Changed to white so it shows on black
    textAlign: 'center',
  },
  bodyText: {
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 16,
    color: '#ccc',  // Changed to light gray for readability
  },
  image: {
    width: '100%',
    height: 200,
    marginBottom: 16,
    borderRadius: 8,
  },
  detailImage: {
    width: '100%',
    height: 250,
    marginVertical: 12,
    borderRadius: 8,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '600',
    marginTop: 16,
    marginBottom: 8,
    color: '#fff',  // Changed to white
  },
});