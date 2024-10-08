import LoginButton from "./components/LoginButton";
import LogoutButton from "./components/LogoutButton";
import Profile from "./components/Profile";

//console.log("App.js");

function App() {
  return (
    <main className="column">
      <h1>Auth0 Login</h1>
      <LoginButton/>
      <LogoutButton/>
      <Profile />
    </main>
  );
}

export default App;
