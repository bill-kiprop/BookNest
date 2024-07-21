import React from 'react'
import { createBrowserRouter } from "react-router-dom";
import HotelLists from '../hotel_components/hotelLists';

import HotelPage from '../hotel_components/hotelPage';
import Home from '../hotel_components/Home';
import Login from '../components/Login';
import Signup from '../components/Signup';

const route = createBrowserRouter([
   {
    path:'/',
    element:<Home/>
   } ,
   {
    path:"/properties",
    element:<HotelLists/>
   },
   {
    path:'/properties/:id',
    element:<HotelPage/>
   },
   {
      path:'/login',
      element:<Login/>
   },{
      path:'/signup',
      element:<Signup/>
   }
])
  

export default route