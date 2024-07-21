import React, { useContext } from 'react';
import { AuthContext } from './AuthContext';
import { useParams, useHistory } from 'react-router-dom';
import { deleteProperty } from './apiService';

const DeleteProperty = () => {
  const { user } = useContext(AuthContext);
  const { id } = useParams();
  const history = useHistory();

  const handleDelete = async () => {
    if (user?.role !== 'host') {
      alert('Only hosts can delete properties.');
      return;
    }
    try {
      await deleteProperty(id);
      alert('Property deleted successfully');
      history.push('/properties');
    } catch (error) {
      alert('Failed to delete property');
    }
  };

  return (
    <button onClick={handleDelete}>Delete Property</button>
  );
};

export default DeleteProperty;
