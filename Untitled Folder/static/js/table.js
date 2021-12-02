console.log("hello table");
const tableBody = document.getElementById("spouse-table-body");
const modalbody = document.getElementById("spouse-modal-body");
const url = window.location.href;
console.log(url);

$.ajax({
  type: "GET",
  url: "/profiles/data-json/",
  success: function (response) {
    console.log(response);
    const data = JSON.parse(response.data);
    console.log(data);
    data.forEach((el) => {
      console.log(el.fields);
      tableBody.innerHTML += `
        <tr>
        <td class="pointer"><div data-bs-toggle="modal" data-bs-target="#spouseModal" data-fname=${el.fields.first_name} class="spouse-fname">${el.fields.first_name}</div></td>
         <td>${el.fields.last_name}</td>
         <td>${el.fields.id_no}</td>
         <td>${el.fields.email}</td>
         <td>${el.fields.phone}</td>
         <td>${el.fields.street}</td>
        </tr>
        `;
    });
    const spouseName = [...document.getElementsByClassName("spouse-fname")];
    console.log(spouseName);
    spouseName.forEach((item) =>
      item.addEventListener("click", (e) => {
        const spouse = e.target.getAttribute("data-fname");
        console.log(spouse);
        modalbody.innerHTML = `<p class="lead"> <span>Name:</span> ${spouse}</p>`;
      })
    );
  },
  error: function (error) {
    console.log(error);
  },
});
