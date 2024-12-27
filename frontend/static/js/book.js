document.addEventListener("DOMContentLoaded", () => {
  flight_duration();
});

function flight_duration() {
  document.querySelectorAll(".duration").forEach((element) => {
    let time = element.dataset.value.split(":");
    element.innerText = time[0] + "h " + time[1] + "m";
  });
}

function add_traveller() {
  let div = document.querySelector(".add-traveller-div");
  let fname = div.querySelector("#fname");
  let lname = div.querySelector("#lname");
  let gender = div.querySelectorAll(".gender");
  let gender_val = null;
  if (fname.value.trim().length === 0) {
    alert("Please enter First Name.");
    return false;
  }

  if (lname.value.trim().length === 0) {
    alert("Please enter Last Name.");
    return false;
  }

  if (!gender[0].checked) {
    if (!gender[1].checked) {
      alert("Please select gender.");
      return false;
    } else {
      gender_val = gender[1].value;
    }
  } else {
    gender_val = gender[0].value;
  }

  let passengerCount = div.parentElement.querySelectorAll(
    ".each-traveller-div .each-traveller"
  ).length;

  let traveller = `<div class="row each-traveller">
                        <div>
                            <span class="traveller-name">${fname.value} ${
    lname.value
  }</span><span>,</span>
                            <span class="traveller-gender">${gender_val.toUpperCase()}</span>
                        </div>
                        <input type="hidden" name="passenger${
                          passengerCount + 1
                        }FName" value="${fname.value}">
                        <input type="hidden" name="passenger${
                          passengerCount + 1
                        }LName" value="${lname.value}">
                        <input type="hidden" name="passenger${
                          passengerCount + 1
                        }Gender" value="${gender_val}">
                        <div class="delete-traveller">
                            <button class="btn" type="button" onclick="del_traveller(this)">
                                <svg width="1.1em" height="1.1em" viewBox="0 0 16 16" class="bi bi-x-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                    <path fill-rule="evenodd" d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
                                </svg>
                            </button>
                        </div>
                    </div>`;
  div.parentElement.querySelector(".each-traveller-div").innerHTML += traveller;
  div.parentElement.querySelector("#p-count").value = passengerCount + 1;
  div.parentElement.querySelector(".traveller-head h6 span").innerText =
    passengerCount + 1;
  div.parentElement.querySelector(".no-traveller").style.display = "none";
  fname.value = "";
  lname.value = "";
  gender.forEach((radio) => {
    radio.checked = false;
  });

  let pcount = document.querySelector("#p-count").value;
  let fare = document.querySelector("#basefare").value;
  let fee = document.querySelector("#fee").value;
  if (parseInt(pcount) !== 0) {
    document.querySelector(".base-fare-value span").innerText =
      parseInt(fare) * parseInt(pcount);
    document.querySelector(".total-fare-value span").innerText =
      parseInt(fare) * parseInt(pcount) + parseInt(fee);
  }
}

function del_traveller(btn) {
  let traveller = btn.parentElement.parentElement;
  let tvl = btn.parentElement.parentElement.parentElement.parentElement;
  let cnt = tvl.querySelector("#p-count");
  cnt.value = parseInt(cnt.value) - 1;
  tvl.querySelector(".traveller-head h6 span").innerText = cnt.value;
  if (parseInt(cnt.value) <= 0) {
    tvl.querySelector(".no-traveller").style.display = "block";
  }
  traveller.remove();

  let pcount = document.querySelector("#p-count").value;
  let fare = document.querySelector("#basefare").value;
  let fee = document.querySelector("#fee").value;
  if (parseInt(pcount) !== 0) {
    document.querySelector(".base-fare-value span").innerText =
      parseInt(fare) * parseInt(pcount);
    document.querySelector(".total-fare-value span").innerText =
      parseInt(fare) * parseInt(pcount) + parseInt(fee);
  }
}

function book_submit() {
  let pcount = document.querySelector("#p-count");
  if (parseInt(pcount.value) > 0) {
    return true;
  }
  alert("Please add atleast one passenger.");
  return false;
}
// Utility function to check if today's date is within a given range
function isTodayInRange(startDate, endDate) {
  const today = new Date();
  return today >= new Date(startDate) && today <= new Date(endDate);
}

function discount() {
  const coupons = { FL928K: 0.3, FL239D: 0.4, FL138S: 0.2 };
  let couponApplied = false; // Flag to track if a coupon has been applied
  let couponCodeApplied = ""; // Store the applied coupon code for removal
  // Get the value of the coupon input field
  const couponInput = document.querySelector('input[name="coupon"]');
  const couponCode = couponInput.value.trim();

  // Check if a coupon is already applied
  if (couponApplied) {
    alert(
      `A coupon is already applied: "${couponCodeApplied}". Please remove it first to enter another coupon.`
    );
    return;
  }

  // Check if the coupon code is not empty
  if (couponCode) {
    // Special validation for FL138S
    if (couponCode === "FL138S") {
      if (!isTodayInRange("2025-01-01", "2025-03-01")) {
        alert(
          'Coupon "FL138S" can only be applied between 01/01/2025 and 03/01/2025.'
        );
        couponInput.value = ""; // Clear the input field so user can try again
        return; // Exit early without applying the coupon
      }
    }

    // Check if the coupon code exists in the coupons dictionary
    if (coupons[couponCode]) {
      const discount = coupons[couponCode]; // Get the discount value from the coupons dictionary

      // Create a new HTML block for the coupon with a remove button
      const couponHtml = `
                <div class="row surcharges" id="appliedCoupon">
                    <div class="surcharges-label">
                        Coupon: ${couponCode} | Discount: ${discount * 100}%
                    </div>
                    <button type="button" id="removeCoupon" class="btn btn-danger btn-sm" style="margin-left: 10px;">Remove</button>
                    <input type="hidden" name="coupon" value="${couponCode}">
                </div>
            `;

      // Insert the new HTML block after the surcharges row
      const surchargesElement = document.querySelector(".surcharges");
      if (surchargesElement) {
        surchargesElement.insertAdjacentHTML("afterend", couponHtml);
      }

      // Optionally clear the input field after applying the coupon
      couponInput.value = "";

      // Mark that a coupon has been applied and store the coupon code
      couponApplied = true;
      couponCodeApplied = couponCode;

      // Disable the input field to prevent further coupon entry
      couponInput.disabled = true;

      // Add event listener to the remove button to allow the user to remove the coupon
      document
        .querySelector("#removeCoupon")
        .addEventListener("click", function () {
          // Remove the coupon HTML block
          const couponElement = document.querySelector("#appliedCoupon");
          if (couponElement) {
            couponElement.remove();
          }

          // Enable the input field again for new coupon
          couponInput.disabled = false;

          // Reset the flag and allow the user to enter a new coupon
          couponApplied = false;
          couponCodeApplied = "";
          couponInput.value = ""; // Clear the input field
        });
    } else {
      alert("Invalid coupon code.");
      couponInput.value = ""; // Clear the input field so user can try again
    }
  } else {
    alert("Please enter a valid coupon code.");
  }
}

// Lắng nghe sự kiện khi người dùng click vào ghế
document.querySelectorAll(".css-19x5fzk").forEach(function (seatElement) {
  seatElement.addEventListener("click", function () {
    // Lấy ID của ghế
    var seatId = seatElement.id.split("-")[1];
    // Lấy giá của ghế từ input hidden
    var price = document.getElementById("price-" + seatId).value;
    // Cập nhật tiền vào phần tử #count
    document.getElementById("count").innerText = price;
  });
});
