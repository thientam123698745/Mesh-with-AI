
const renderTemp = async () => {
  const temp = document.getElementById("temp");
  const humi = document.getElementById("humi");
  const res = await fetch("/status");
  const data = await res.json();
  console.log(data);
  try {
    temp.innerHTML ="Nhiệt độ 2:</br>" + data[1] + "&deg;C";
    humi.innerHTML = "Nhiệt độ 1:</br>" + data[0] + "&deg;C";
  } catch (err) {
    console.log("err", err);
  }
};

setInterval(() => {
  renderTemp();
}, 5000);


const date = document.getElementById("date");

const dateDisplay = async () => {
  date.innerHTML = new Date().toLocaleString('en-US', { timeZone: 'Asia/Ho_Chi_Minh' });
};

setInterval(() => {
  dateDisplay();
}, 1000);

const fanStatus = document.getElementById("fan");
fanStatus.addEventListener("click", handleFan);


async function handleFan() {
  fanStatus.setAttribute('disabled', true);
  setTimeout( async () => {
    fanStatus.removeAttribute('disabled');
  }, 3000);
  const value = fanStatus.checked ? '1' : '0';
  await fetch('/fan', {
    method: 'POST',
    body: value
  })
    .then(response => {
      if (response.ok && response.statusText == 'OK') {
        console.log('Yêu cầu POST thành công');
      } else {
        console.error('Yêu cầu POST thất bại');
      }
    })
    .catch(error => {
      console.error('Lỗi trong quá trình gửi yêu cầu POST', error);
    });
}

const getFanStatus = async () => {
  // Get fan status from server "/fanstatus"
  const res = await fetch('/fanstatus');
  const data = await res.json();
  return data;
}

const renderFanStatus = async () => {
  const temp = await getFanStatus();
  fanStatus.checked = temp;
}

renderFanStatus();
setInterval(() => {
  renderFanStatus();
}, 1000);