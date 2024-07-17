import React, { useState, useEffect } from 'react';
import './Carousel.css'; // Import your CSS file for styling

const Carousel = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const slides = [
    'https://cdn.ramseysolutions.net/media/blog/saving/travel-and-vacation/staycation-ideas.jpg',
    'https://t4.ftcdn.net/jpg/03/65/54/79/360_F_365547989_SBROeZWm90Z8b3WALedUclIsRR3xxzXF.jpg',
    // Add more image URLs as needed
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      // Move to the next slide
      setCurrentSlide((prevSlide) => (prevSlide === slides.length - 1 ? 0 : prevSlide + 1));
    }, 3000); // Change slide every 3 seconds (adjust as needed)

    // Cleanup interval on component unmount
    return () => clearInterval(interval);
  }, [slides.length]); // Depend on slides.length to re-run effect when slides change

  return (
    <div id="carouselExampleControls" className="carousel slide" data-ride="carousel">
      <div className="carousel-inner">
        {slides.map((slide, index) => (
          <div key={index} className={`carousel-item ${index === currentSlide ? 'active' : ''}`}>
            <img className="d-block w-100" src={slide} alt={`Slide ${index + 1}`} />
          </div>
        ))}
      </div>
      <a className="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
        <span className="sr-only">Previous</span>
      </a>
      <a className="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
        <span className="carousel-control-next-icon" aria-hidden="true"></span>
        <span className="sr-only">Next</span>
      </a>
    </div>
  );
};

export default Carousel;
