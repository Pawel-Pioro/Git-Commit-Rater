import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App baseUrl="http://127.0.0.1:8000/api/" />
  </React.StrictMode>,
)
