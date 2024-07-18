// src/pages/Reviews.jsx
import React, { useEffect, useState } from 'react';
import { Container, Form, Button, ListGroup, Alert } from 'react-bootstrap';
//import { useAuth } from '../auth'; // Custom hook for authentication
//import { getReviews, postReview } from '../api'; 

const Reviews = () => {
  const { isAuthenticated } = useAuth();
  const [reviews, setReviews] = useState([]);
  const [newReview, setNewReview] = useState('');
  const [rating, setRating] = useState(1);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch reviews when component mounts
    const fetchReviews = async () => {
      try {
        const response = await getReviews();
        setReviews(response.data);
      } catch (err) {
        console.error('Failed to fetch reviews:', err);
      }
    };

    fetchReviews();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isAuthenticated()) {
      alert('You need to be logged in to leave a review.');
      return;
    }
    
    try {
      await postReview({ text: newReview, rating });
      setNewReview('');
      setRating(1);
      const response = await getReviews();
      setReviews(response.data);
    } catch (err) {
      setError('Failed to submit review.');
    }
  };

  const averageRating = reviews.reduce((acc, review) => acc + review.rating, 0) / reviews.length || 0;

  return (
    <Container>
      <h2 className="my-4">Reviews</h2>
      {error && <Alert variant="danger">{error}</Alert>}
      <Form onSubmit={handleSubmit} className="mb-4">
        <Form.Group controlId="formReview">
          <Form.Label>Leave a review</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            value={newReview}
            onChange={(e) => setNewReview(e.target.value)}
            placeholder="Write your review here"
            required
          />
        </Form.Group>
        <Form.Group controlId="formRating">
          <Form.Label>Rating</Form.Label>
          <Form.Control
            as="select"
            value={rating}
            onChange={(e) => setRating(Number(e.target.value))}
            required
          >
            {[1, 2, 3, 4, 5].map(num => (
              <option key={num} value={num}>{num}</option>
            ))}
          </Form.Control>
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit Review
        </Button>
      </Form>
      <h3>Average Rating: {averageRating.toFixed(1)} / 5</h3>
      <ListGroup>
        {reviews.map((review, index) => (
          <ListGroup.Item key={index}>
            <strong>Rating:</strong> {review.rating} <br />
            <strong>Review:</strong> {review.text}
          </ListGroup.Item>
        ))}
      </ListGroup>
    </Container>
  );
};

export default Reviews;
