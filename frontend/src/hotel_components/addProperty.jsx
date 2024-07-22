import React, { useState } from 'react';
import axios from 'axios';
import './addproperty.css'

const AddPropertyModal = ({ isOpen, onClose }) => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [address, setAddress] = useState('');
    const [images, setImages] = useState('');  // Assuming images is a URL or a path

    const handleAddProperty = async (event) => {
        event.preventDefault();

        const token = localStorage.getItem('token'); // Assuming JWT token is stored in localStorage

        try {
            const response = await axios.post(
                'http://localhost:5000/properties',
                { name, description, address, images },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            console.log(response.data);
            onClose();
        } catch (error) {
            console.error('There was an error!', error);
        }
    };

    if (!isOpen) return null;

    return (
        <div className="modal">
            <div className="modal-content">
                <span className="close" onClick={onClose}>&times;</span>
                <h2>Add New Property</h2>
                <form onSubmit={handleAddProperty}>
                    <label>
                        Name:
                        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
                    </label>
                    <label>
                        Description:
                        <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} required />
                    </label>
                    <label>
                        Address:
                        <input type="text" value={address} onChange={(e) => setAddress(e.target.value)} required />
                    </label>
                    <label>
                        Images:
                        <input type="text" value={images} onChange={(e) => setImages(e.target.value)} required />
                    </label>
                    <button type="submit" className=''>Add Property</button>
                </form>
            </div>
        </div>
    );
};

export default AddPropertyModal;
