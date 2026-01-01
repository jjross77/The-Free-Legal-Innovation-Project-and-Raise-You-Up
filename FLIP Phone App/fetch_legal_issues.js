
function fetch_legal_issues({ item }) {
  const {
    id, name, avatar, phone,
  } = item;

  return (
    <ContactListItem
      name={name}
      avatar={avatar}
      phone={phone}
      onPress={() => {
        // Pass and merge params back to home screen
        navigation.navigate({
          name: 'library3',
          params:  { user: 'jane' },
        });
      }}
      />

  );
};
