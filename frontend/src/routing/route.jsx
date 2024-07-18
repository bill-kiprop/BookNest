import React from 'react'
import { createBrowserRouter } from "react-router-dom";
import HotelLists from '../hotel_components/hotelLists';
import App from '../App';
import HotelPage from '../hotel_components/hotelPage';

const route = createBrowserRouter([
   {
    path:'/',
    element:<App/>
   } ,
   {
    path:"/properties",
    element:<HotelLists/>
   },
   {
    path:'/properties/:id',
    element:<HotelPage/>
   }
])
  

export default route