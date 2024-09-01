import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Auth0Provider } from '@auth0/auth0-react';

const domain = process.env.REACT_APP_AUTH0_DOMAIN;
const clientId = process.env.REACT_APP_AUTH0_CLIENT_ID;

//console.log('Domain:', domain);
//console.log('Client ID:', clientId);

ReactDOM.render(
  <React.StrictMode>
    <Auth0Provider
      domain={domain}
      //domain="dev-kq274kq68l2v8hrl.us.auth0.com"
      clientId={clientId}
      //clientId="4bgNyMJ2LqfA9H1exKYRS8BY10JaM9be"
      redirectUri={window.location.origin}
    >
    <App />
    </Auth0Provider>
  </React.StrictMode>,
  document.getElementById('root')
);


