import React from 'react'
import ReactDOM from 'react-dom/client'
import 'bootstrap/dist/css/bootstrap.min.css';


import './index.css'
import { RouterProvider } from 'react-router-dom';
import route from './routing/route.jsx';


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router = {route}/>
  </React.StrictMode>,
)
