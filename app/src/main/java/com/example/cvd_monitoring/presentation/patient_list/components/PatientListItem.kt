package com.example.cvd_monitoring.presentation.patient_list.components

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import com.example.cvd_monitoring.domain.model.users.Patient

@Composable
fun PatientListItem(patient: Patient) {
    Card(
        modifier = Modifier
            .padding(8.dp, 4.dp)
            .fillMaxWidth()
            .height(110.dp),
        shape = MaterialTheme.shapes.medium
    ) {
        Row(
            Modifier
                .padding(4.dp)
                .fillMaxSize()
        ) {

            Column(
                verticalArrangement = Arrangement.Center,
                modifier = Modifier
                    .padding(4.dp)
                    .fillMaxHeight()
                    .weight(0.8f)
            ) {
                Text(
                    text = patient.user.first_name,
                    fontWeight = FontWeight.Bold
                )
                Text(
                    text = patient.user.last_name,
                    modifier = Modifier
                        .background(Color.LightGray)
                        .padding(4.dp)
                )
                Text(
                    text = patient.user.email,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
            }
        }
    }
}