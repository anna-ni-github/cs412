import { StyleSheet, View, Text, Image, TouchableOpacity, ActivityIndicator, ScrollView } from 'react-native';
import { useState, useEffect } from 'react';
import { Ionicons } from '@expo/vector-icons';


const API_BASE_URL = 'http:10.0.0.225';

// Define TypeScript interfaces for our data
interface Joke {
  id: number;
  text: string;
  name: string;
  timestamp: string;
}

interface Picture {
  id: number;
  image_url: string;
  name: string;
  timestamp: string;
}

export default function IndexScreen() {
  // State variables to hold our data
  const [joke, setJoke] = useState<Joke | null>(null);
  const [picture, setPicture] = useState<Picture | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Function to fetch random joke from API
  const fetchRandomJoke = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/random/`);
      if (!response.ok) {
        throw new Error('Failed to fetch joke');
      }
      const data = await response.json();
      setJoke(data);
    } catch (err) {
      console.error('Error fetching joke:', err);
      setError('Failed to load joke');
    }
  };

  // Function to fetch random picture from API
  const fetchRandomPicture = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/random_picture/`);
      if (!response.ok) {
        throw new Error('Failed to fetch picture');
      }
      const data = await response.json();
      setPicture(data);
    } catch (err) {
      console.error('Error fetching picture:', err);
      setError('Failed to load picture');
    }
  };

  // Function to load both joke and picture
  const loadContent = async () => {
    setLoading(true);
    setError(null);
    await Promise.all([fetchRandomJoke(), fetchRandomPicture()]);
    setLoading(false);
  };

  // Load content when component mounts
  useEffect(() => {
    loadContent();
  }, []);

  // Show loading indicator while fetching data
  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color="#667eea" />
        <Text style={styles.loadingText}>Loading dad joke...</Text>
      </View>
    );
  }

  // Show error message if something went wrong
  if (error) {
    return (
      <View style={styles.centerContainer}>
        <Ionicons name="alert-circle" size={64} color="#ff6b6b" />
        <Text style={styles.errorText}>{error}</Text>
        <TouchableOpacity style={styles.retryButton} onPress={loadContent}>
          <Text style={styles.retryButtonText}>Retry</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>🤣 Dad Jokes 🎭</Text>
        <Text style={styles.headerSubtitle}>Random Joke & Picture</Text>
      </View>

      {/* Joke Card */}
      {joke && (
        <View style={styles.card}>
          <View style={styles.cardHeader}>
            <Ionicons name="chatbox-ellipses" size={24} color="#667eea" />
            <Text style={styles.cardTitle}>Today's Joke</Text>
          </View>
          <Text style={styles.jokeText}>{joke.text}</Text>
          <View style={styles.contributorContainer}>
            <Ionicons name="person-circle" size={16} color="#666" />
            <Text style={styles.contributorText}>by {joke.name}</Text>
          </View>
        </View>
      )}

      {/* Picture Card */}
      {picture && (
        <View style={styles.card}>
          <View style={styles.cardHeader}>
            <Ionicons name="image" size={24} color="#764ba2" />
            <Text style={styles.cardTitle}>Silly Picture</Text>
          </View>
          <Image 
            source={{ uri: picture.image_url }} 
            style={styles.image}
            resizeMode="cover"
          />
          <View style={styles.contributorContainer}>
            <Ionicons name="person-circle" size={16} color="#666" />
            <Text style={styles.contributorText}>by {picture.name}</Text>
          </View>
        </View>
      )}

      {/* Refresh Button */}
      <TouchableOpacity style={styles.refreshButton} onPress={loadContent}>
        <Ionicons name="refresh" size={24} color="white" />
        <Text style={styles.refreshButtonText}>Get Another Random Pair</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  contentContainer: {
    padding: 16,
    paddingBottom: 32,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginBottom: 24,
    paddingTop: 8,
  },
  headerTitle: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 4,
  },
  headerSubtitle: {
    fontSize: 16,
    color: '#666',
  },
  card: {
    backgroundColor: 'white',
    borderRadius: 16,
    padding: 20,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  cardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginLeft: 8,
  },
  jokeText: {
    fontSize: 18,
    lineHeight: 28,
    color: '#333',
    marginBottom: 16,
  },
  image: {
    width: '100%',
    height: 250,
    borderRadius: 12,
    marginBottom: 16,
  },
  contributorContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  contributorText: {
    fontSize: 14,
    color: '#666',
    fontStyle: 'italic',
    marginLeft: 6,
  },
  refreshButton: {
    backgroundColor: '#667eea',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
    borderRadius: 12,
    marginTop: 8,
  },
  refreshButtonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
    marginLeft: 8,
  },
  loadingText: {
    marginTop: 16,
    fontSize: 16,
    color: '#666',
  },
  errorText: {
    marginTop: 16,
    fontSize: 16,
    color: '#ff6b6b',
    textAlign: 'center',
    marginBottom: 16,
  },
  retryButton: {
    backgroundColor: '#667eea',
    padding: 12,
    borderRadius: 8,
    paddingHorizontal: 24,
  },
  retryButtonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
});