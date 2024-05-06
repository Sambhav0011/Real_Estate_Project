import { useState } from "react";
import "./searchBar.scss";
import { Link } from "react-router-dom";

const types = ["buy", "rent"];
function SearchBar() {
    const [query, setQuery] = useState({
        type: "buy",
        city: "",
        minPrice: 0,
        maxPrice: 0,
      });
    
      const switchType = (val) => {
        setQuery((prev) => ({ ...prev, type: val }));
      };
      const handleChange = (e) => {
        setQuery((prev) => ({ ...prev, [e.target.name]: e.target.value }));
      };

  return (
    <div className="searchBar">
      <div className="type">
      {types.map((type) => (
          <button
            key={type}
            onClick={() => switchType(type)}
            className={query.type === type ? "active" : ""}
          >
            {type}
          </button>
        ))}
      </div>
      <form>
      <select name="city" onChange={handleChange}>
        <option value="City">City</option>
        <option value="Delhi">Delhi</option>
        <option value="Bangalore">Bangalore</option>
        <option value="Chennai">Chennai</option>
        <option value="Paris">Paris</option>
      </select>
        <input
          type="number"
          name="minPrice"
          min={0}
          max={10000000}
          placeholder="Min Price"
          onChange={handleChange}
        />
        <input
          type="number"
          name="maxPrice"
          min={0}
          max={10000000}
          placeholder="Max Price"
          onChange={handleChange}
        />
        <Link 
        to={`/list?type=${query.type}&city=${query.city}&minPrice=${query.minPrice}&maxPrice=${query.maxPrice}`}>
          <button>
            <img src="/search.png" alt="" />
          </button>
        </Link>

      </form>
    </div>
  );
}

export default SearchBar;