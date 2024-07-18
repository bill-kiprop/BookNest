import React from 'react';

const Carousel = () => {
  return (
    <div id="carouselExampleCaptions" className="carousel slide" data-bs-ride="carousel">
      <div className="carousel-inner">
        <div className="carousel-item active">
          <img
            src="https://cdn.ramseysolutions.net/media/blog/saving/travel-and-vacation/staycation-ideas.jpg"
            className="d-block w-100"
            alt="Slide 1"
          />
          <div className="carousel-caption d-none d-md-block">
            <h5>Stays</h5>
            <p>Unwind in our different stays.</p>
          </div>
        </div>
        <div className="carousel-item">
          <img
            src="https://media.cntraveler.com/photos/6282893c0786ba755ddefa88/16:9/w_3488,h_1962,c_limit/Airbnb%20Host%2000-Lede.jpg"
            className="d-block w-100"
            alt="Slide 2"
          />
          <div className="carousel-caption d-none d-md-block">
            <h5>Cozy cottage</h5>
            <p>A cozy place to stay.</p>
          </div>
        </div>
        <div className="carousel-item">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToS50JPG3gjzdiTjEHTafN9JkeYHtktA04cg&s"
            className="d-block w-100"
            alt="Slide 3"
          />
          <div className="carousel-caption d-none d-md-block">
            <h5>Luxury Suite</h5>
            <p>Experience luxury like never before.</p>
          </div>
        </div>
      </div>
      <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Previous</span>
      </button>
      <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span className="carousel-control-next-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Next</span>
      </button>
    </div>
  );
};

export default Carousel;
