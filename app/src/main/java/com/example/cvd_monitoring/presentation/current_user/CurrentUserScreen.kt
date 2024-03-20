package com.example.cvd_monitoring.presentation.current_user

import android.util.Log
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
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
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController

@Composable
fun CurrentUserScreen(
    viewModel: CurrentUserViewModel = hiltViewModel(),
    navController: NavController,
) {
    val slug = navController.currentBackStackEntry?.arguments?.getString("slug") ?: ""

    LaunchedEffect(key1 = slug) {
        viewModel.getCurrentUser(slug)
    }
    val state = viewModel.state.value
    Card(
        modifier = Modifier
            .padding(8.dp, 4.dp)
            .fillMaxWidth()
            .height(160.dp),
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
                state.patient?.user?.let {
                    Text(
                        text = it.first_name,
                        fontWeight = FontWeight.Bold
                    )
                }
                state.patient?.user?.let {
                    Text(
                        text = it.last_name,
                        modifier = Modifier
                            .background(Color.LightGray)
                            .padding(4.dp)
                    )
                }
                state.patient?.user?.let {
                    Text(
                        text = it.email,
                        maxLines = 2,
                        overflow = TextOverflow.Ellipsis
                    )
                }
                Text(
                    text = state.patient?.age.toString(),
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
                Text(
                    text = state.patient?.weight.toString(),
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
                Text(
                    text = state.patient?.height.toString(),
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
            }
        }
    }
}