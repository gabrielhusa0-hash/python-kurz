import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, FlatList, TextInput } from 'react-native';
import { Ionicons, MaterialCommunityIcons, Octicons } from '@expo/vector-icons'; 

const chatData = [
  {
    id: '1',
    name: 'Sindy',
    avatar: 'https://as2.ftcdn.net/v2/jpg/03/75/80/95/1000_F_375809542_p5kAuI4VhG7dMjp8WAmjvPHRwy5Iyccd.jpg',
    lastMessage: 'Prosím, někdo mi prosím pomozte opravit chybu v aplikaci',
    time: 'Neděle',
    unreadCount: 0,
    read: true,
    hasStory: false,
    isOfficial: false,
    online: false, 
  },
  {
    id: '2',
    name: 'Patrik',
    avatar: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150',
    lastMessage: 'Zmeškaný hovor',
    time: 'Pátek',
    unreadCount: 2,
    read: false,
    missed: true,
    hasStory: false,
    isOfficial: false,
    isOnline: true,
    online: true,
  },
  {
    id: 'w_official',
    name: 'WhatsApp',
    avatar: 'https://tse2.mm.bing.net/th/id/OIP.v6ezNoTSWw_olOqM9AcnMwHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3', 
    lastMessage: '• Novinka: Buďte o krok napřed díky upozorněním na připojených...',
    time: 'Pátek',
    unreadCount: 1,
    read: false,
    hasStory: false,
    isOfficial: true,
  },
  {
    id: '3',
    name: 'Anna',
    avatar: 'https://i.pinimg.com/originals/1e/db/d7/1edbd7f7c930a3e9c6b8701c527a708b.jpg',
    lastMessage: 'Dobré ráno, Richarde, že jsi dokončil projekt, který jsem ti dal...',
    time: '6/23/2026',
    unreadCount: 0,
    read: false,
    hasStory: true,
    isOfficial: true,
    isOnline:  true,
  },
  {
    id: '4',
    name: 'Viktor',
    avatar: 'https://datingacrosscultures.com/wp-content/uploads/2023/10/How-Do-German-Guys-Flirt.-Unlocking-The-Charms-Of-German-Men.jpg',
    lastMessage: 'Poslal jsem ti včerejší zprávu, prosím, podívej se na ni a informuj mě',
    time: '6/22/2026',
    unreadCount: 0,
    read: false,
    hasStory: false,
    isOfficial: false,
  },
  {
     id: '5',
   name: 'Klaus Zimmermann',
   avatar: 'https://imgcdn.stablediffusionweb.com/2024/11/25/220e6829-dd0c-464c-b764-2fd070a37b37.jpg',
   lastMessage: 'Alles Gute 😀 ',
   time: '6/21/2026',
   unreadCount: 0,
   read: true,
   hasStory: true,
   isOfficial: false, 
  },
  {
    id: '6',
    name: 'Ben',
    avatar: 'https://freepngimg.com/download/logo/69605-kali-brand-balvano-mossa-black-linux-logo.png',
    lastMessage: 'Máš logy? Bez nich se těžko pozná, co se děje',
    time: '6/20/2026',
    unreadCount: 0,
    read: false,
    hasStory: false,
    isOfficial: false,
  },
];

const ChatItem = ({ item }) => (
  <View style={styles.chatItem}>
    <View style={item.hasStory ? styles.avatarStoryContainer : styles.avatarContainer}>
      <Image source={{ uri: item.avatar }} style={styles.avatar} />
    </View>

    <View style={styles.chatInfo}>
      <View style={styles.chatRow}>
        <Text style={[styles.name, item.isOfficial ? styles.officialName : null]}>{item.name}</Text>
        <Text style={[styles.time, item.unreadCount > 0 ? styles.timeUnread : null]}>{item.time}</Text>
      </View>
      <View style={styles.chatRow}>
        <View style={styles.messageContent}>
          {item.read && (
            <MaterialCommunityIcons name="check-all" size={16} color="#53bdeb" style={styles.ticksIcon} />
          )}
          {item.missed && (
            <MaterialCommunityIcons name="phone-missed" size={15} color="#f15c6d" style={styles.missedPhoneIcon} />
          )}
          <Text style={[styles.lastMessage, item.missed ? styles.missedMessage : null, item.isOfficial ? styles.officialMessage : null]} numberOfLines={1}>
            {item.lastMessage}
          </Text>
        </View>
        {item.unreadCount > 0 && (
          <View style={styles.unreadBadge}>
            <Text style={styles.unreadCountText}>{item.unreadCount}</Text>
          </View>
        )}
      </View>
    </View>
  </View>
);

export default function App() {
  return (
    <View style={styles.mainContainer}>
      <StatusBar style="light" />

      {/* LEVÁ LIŠTA */}
      <View style={styles.sidebar}>
        <View style={styles.sidebarTopIcons}>
          <View style={styles.downloadIconContainer}>
            <MaterialCommunityIcons name="download-box-outline" size={24} color="#aebac1" />
          </View>
          <View style={styles.sidebarDivider} />

          <MaterialCommunityIcons name="message-text" size={22} color="#00a884" style={styles.sidebarIconActive} />
          <Ionicons name="call-outline" size={22} color="#aebac1" style={styles.sidebarIcon} />
          <Octicons name="circle-slash" size={20} color="#aebac1" style={styles.sidebarIcon} />
          <Ionicons name="star-outline" size={21} color="#aebac1" style={styles.sidebarIcon} />
          <MaterialCommunityIcons name="archive-outline" size={22} color="#aebac1" style={styles.sidebarIcon} />
          <Ionicons name="people-outline" size={22} color="#aebac1" style={styles.sidebarIcon} />
        </View>

        <View style={styles.sidebarBottomIcons}>
          <View style={styles.sidebarDivider} />
          <MaterialCommunityIcons name="layers-outline" size={22} color="#aebac1" style={styles.layersIcon} />
          <View style={[styles.sidebarDivider, { marginBottom: 10 }]} />
          
          <Ionicons name="settings-outline" size={22} color="#aebac1" style={styles.sidebarIcon} />
          <Image 
            source={{ uri: 'https://logodix.com/logo/2085375.png' }} 
            style={styles.sidebarAvatar} 
          />
        </View>
      </View>

      {/* HLAVNÍ OBSAH */}
      <View style={styles.container}>
        <View style={styles.header}>
          <Text style={styles.headerTitle}>Chaty</Text>
          <View style={styles.headerIcons}>
            <Ionicons name="create-outline" size={22} color="#fff" style={styles.icon} />
            <Ionicons name="ellipsis-vertical" size={20} color="#fff" />
          </View>
        </View>

        <View style={styles.searchContainer}>
          <View style={styles.searchBar}>
            <Ionicons name="search-outline" size={16} color="#8696a0" style={styles.searchIcon} />
            <TextInput 
              style={styles.searchInput} 
              placeholder="Vyhledejte chat nebo zahajte nový" 
              placeholderTextColor="#8696a0"
              editable={false} // Změň na true, pokud chceš povolit psaní
            />
          </View>
        </View>

        <View style={styles.filterContainer}>
          <View style={styles.activeFilter}>
            <Text style={styles.activeFilterText}>Vše</Text>
          </View>
          <View style={styles.inactiveFilter}>
            <Text style={styles.inactiveFilterText}>Nepřečtené 3</Text>
          </View>
          <View style={styles.inactiveFilter}>
            <Text style={styles.inactiveFilterText}>Oblíbené</Text>
          </View>
          <View style={styles.inactiveFilter}>
            <Text style={styles.inactiveFilterText}>Skupiny</Text>
          </View>
          <View style={styles.plusFilter}>
            <Text style={styles.inactiveFilterText}>+</Text>
          </View>
        </View>

        <View style={styles.content}>
          <FlatList
            data={chatData}
            renderItem={({ item }) => <ChatItem item={item} />}
            keyExtractor={item => item.id}
            style={styles.chatList}
          />
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  mainContainer: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: '#111b21',
  },
  sidebar: {
    width: 60,
    backgroundColor: '#202c33',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 15,
    borderRightWidth: 1,
    borderRightColor: '#2f3b43',
  },
  sidebarTopIcons: {
    alignItems: 'center',
    gap: 20,
    width: '100%',
  },
  sidebarBottomIcons: {
    alignItems: 'center',
    gap: 18,
    width: '100%',
  },
  downloadIconContainer: {
    marginTop: 5,
    opacity: 0.8,
  },
  layersIcon: {
    opacity: 0.8,
    marginVertical: 4,
  },
  sidebarDivider: {
    width: '70%',
    height: 1,
    backgroundColor: '#2f3b43',
    marginVertical: 4,
  },
  sidebarIcon: {
    opacity: 0.8,
  },
  sidebarIconActive: {
    color: '#00a884',
  },
  sidebarAvatar: {
    width: 28,
    height: 28,
    borderRadius: 14,
    marginTop: 5,
  },
  container: {
    flex: 1,
  },
  header: {
    paddingTop: 20,
    paddingBottom: 10,
    paddingHorizontal: 16,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  headerTitle: {
    color: '#e9edef',
    fontSize: 22,
    fontWeight: 'bold',
  },
  headerIcons: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  icon: {
    marginRight: 15,
  },
  searchContainer: {
    paddingHorizontal: 16,
    paddingBottom: 12,
  },
  searchBar: {
    backgroundColor: '#202c33',
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 8,
  },
  searchIcon: {
    marginRight: 12,
  },
  searchInput: {
    color: '#aebac1',
    fontSize: 13,
    flex: 1,
  },
  filterContainer: {
    flexDirection: 'row',
    paddingHorizontal: 16,
    paddingBottom: 12,
    gap: 6,
    alignItems: 'center',
  },
  activeFilter: {
    backgroundColor: '#0a332c',
    paddingVertical: 5,
    paddingHorizontal: 12,
    borderRadius: 14,
  },
  activeFilterText: {
    color: '#00a884',
    fontWeight: '600',
    fontSize: 13,
  },
  inactiveFilter: {
    backgroundColor: '#202c33',
    paddingVertical: 5,
    paddingHorizontal: 12,
    borderRadius: 14,
  },
  inactiveFilterText: {
    color: '#8696a0',
    fontWeight: '600',
    fontSize: 13,
  },
  plusFilter: {
    backgroundColor: '#202c33',
    width: 26,
    height: 26,
    borderRadius: 13,
    justifyContent: 'center',
    alignItems: 'center',
  },
  content: {
    flex: 1,
  },
  chatList: {
    flex: 1,
  },
  chatItem: {
    flexDirection: 'row',
    paddingVertical: 10,
    paddingHorizontal: 16,
  },
  avatarContainer: {
    padding: 2,
  },
  avatarStoryContainer: {
    borderWidth: 2,
    borderColor: '#00a884',
    borderRadius: 28,
    padding: 1,
  },
  avatar: {
    width: 44,
    height: 44,
    borderRadius: 22,
  },
  chatInfo: {
    flex: 1,
    justifyContent: 'center',
    marginLeft: 12,
    borderBottomWidth: 0.5,
    borderBottomColor: '#222d34',
    paddingBottom: 10,
  },
  chatRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 2,
  },
  name: {
    color: '#e9edef',
    fontSize: 15,
    fontWeight: '400',
  },
  officialName: {
    fontWeight: '600',
  },
  time: {
    color: '#8696a0',
    fontSize: 11,
  },
  timeUnread: {
    color: '#00a884',
  },
  messageContent: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
    marginRight: 10,
  },
  ticksIcon: {
    marginRight: 3,
  },
  missedPhoneIcon: {
    marginRight: 4,
  },
  lastMessage: {
    color: '#8696a0',
    fontSize: 13,
    flex: 1,
  },
  officialMessage: {
    color: '#e9edef',
  },
  missedMessage: {
    color: '#f15c6d',
  },
  unreadBadge: {
    backgroundColor: '#00a884',
    width: 18,
    height: 18,
    borderRadius: 9,
    justifyContent: 'center',
    alignItems: 'center',
  },
  unreadCountText: {
    color: '#111b21',
    fontSize: 10,
    fontWeight: '700',
  },
});